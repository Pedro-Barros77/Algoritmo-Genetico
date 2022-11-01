from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from matplotlib.pyplot import draw, gca
from frontend.resources.icons_qrc import icons
from frontend.resources.imgs import background_img
from frontend.menu import Ui_MainWindow
from frontend.menu import *
from frontend.functions import functionalities
from backend.models import _models as models


import backend.genetic_algorithm as gen_alg
from datetime import datetime, timedelta


class menu_principal(QMainWindow, Ui_MainWindow):
    """The main window of the application.
    """
    def __init__(self):
        super(menu_principal,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.app_functions = functionalities(self)
        self.running_thread = None
        self.ui.btn_toggle_burguer.clicked.connect(self.app_functions.toggle_left_menu)
        self.ui.btn_start_restart.clicked.connect(self.start)
        self.ui.btn_cancel.clicked.connect(self.cancel)
        self.ui.btn_view_graph.clicked.connect(self.show_graph)
            
    @pyqtSlot()
    def start(self):
        """Starts Genetic Algorithm process
        """
        if self.running_thread != None:
            self.cancel()
            sleep(1)
        self.input_values = {
            'population': self.ui.spinbox_population.value(),
            'total_genes':self.ui.spinbox_total_genes.value(),
            'max_genes': self.ui.spinbox_max_genes.value(),
            'min_genes': self.ui.spinbox_min_genes.value(),
            'target_perc':(self.ui.spinbox_taget_percentage.value() / 100),
            'min_succeed':self.ui.spinbox_min_succeeded.value(),
            'chosen_perc': (self.ui.spinbox_chosen_percentage.value() / 100),
            'mutation_perc': (self.ui.spinbox_mutation_percentage.value() / 100),
        }
        if self.ui.spinbox_min_succeeded.value() > self.ui.spinbox_population.value():
            print('ERRO! min não pode ser menor que o total population')
            return
        self.has_mutation = self.input_values['mutation_perc'] > 0
        self.data = models.data()
        self.last_update = datetime.now()
        self.start_time = datetime.now()
        self.running_thread = gen_alg.GeneticAlgorithm(self.input_values) 
        self.running_thread.resultAvailable.connect(self.result_ready)
        self.running_thread.startup_callback.connect(self.app_functions.update_lbl_perfect_min)
        self.running_thread.colocation_callback.connect(self.new_placement)
        self.running_thread.start()
        self.has_legend = False
        self.ui.btn_start_restart.setText("Restart")
        self.ui.btn_cancel.setDisabled(False)
       
      
    @pyqtSlot()
    def cancel(self):
        """Cancels Genetic Algorithm process
        """
        if self.running_thread == None:
            return
        self.running_thread.stop()
        self.app_functions.cancel()
        
        
    @pyqtSlot(object)
    def new_placement(self, podium):
        self.app_functions.placement(podium)
        
 
    @pyqtSlot(object)
    def result_ready(self, result):
        """Callback connected to gen_alg.GeneticAlgorithm.resultAvailable

        Args:
            data (Data): A set of information provided by GeneticAlgorithm about the progress of the process.
        """
        
        if result["is_Alive"] == False:
            return
        if datetime.now() < self.last_update.__add__(timedelta(milliseconds=150)):
            return
        self.last_update = datetime.now()
        
        self.app_functions.info_plt_axes.clear()
        
        _delta = datetime.now() - self.start_time
        _elapsed = int(_delta.total_seconds() * 1000)
        
        _best = result["bestscore"]
        _gens = result["generations"]
        _muts = result["mutations"]
        self.data.bestscores_list.append(_best)
        self.data.generations_list.append(_gens)
        self.data.mutations_list.append(_muts)
        self.data.time_list.append(_elapsed)

        self.app_functions.info_plt_axes.plot(self.data.time_list, self.data.bestscores_list)
        self.app_functions.info_plt_axes.plot(self.data.time_list, self.data.generations_list)

        if self.has_mutation:
            self.app_functions.info_plt_axes.plot(self.data.time_list, self.data.mutations_list)
        
        if not self.has_legend:
            self.app_functions.info_plt.legend(['Best Score','Generations','Mutations'],loc = 'upper left', bbox_to_anchor=(0.13, 0.87))
            self.has_legend = True
            
        self.app_functions.canvas.draw()
        self.app_functions.update_info_labels(result)    

    
    def show_graph(self):
        print("Em desenvolvimento")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)        
    window = menu_principal()
    window.show()
    sys.exit(app.exec_())

