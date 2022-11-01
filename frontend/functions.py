import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import matplotlib
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


from frontend.menu import *
import backend.genetic_algorithm as gen_alg
from backend.models import _models as models


class functionalities():
    def __init__(self, app):
        self.app = app
    
        #Creates and adds graphic to the frame
        self.info_plt = plt.figure(figsize=(5, 4), dpi=100)
        self.info_plt_axes = self.info_plt.add_subplot(111)
        self.canvas = FigureCanvas(self.info_plt)
        lay = QtWidgets.QVBoxLayout(self.app.ui.center_superior_frame_csf)
        lay.addWidget(self.canvas)

    def update_info_labels(self,result):
        self.app.ui.lbl_gens_value.setText(str(result["generations"]))
        self.app.ui.lbl_best_score_value.setText(str(result["bestscore"]))
        self.app.ui.lbl_muts_value.setText(str(result["mutations"]))
        self.app.ui.lbl_worst_score_value.setText(str(result["worst_score"]))
        _delta = datetime.datetime.now() - self.app.start_time
        self.app.ui.lbl_elapsed_time_value.setText(str(datetime.timedelta(seconds=_delta.total_seconds()))[2:-3])
    def update_lbl_perfect_min(self, result):
        
        self.app.ui.lbl_perfect_value.setText(str(result["perfect_value"]))
        self.app.ui.lbl_min_succeed_value.setText(str(result["minimal_value"]))


    def toggle_left_menu(self):
        """Opens/Closes left menu on hamburguer icon click.

        Args:
            left_menu (QtWidgets.QFrame): The frame containing left menu.
        """
        menu_width = self.app.ui.left_menu.width()

        if menu_width == 50:
            new_width = 300
            
        else:
            new_width = 50
        
        self.animation_left_menu = QtCore.QPropertyAnimation(self.app.ui.left_menu, b"maximumWidth")
        self.animation_left_menu.setDuration(500)
        self.animation_left_menu.setStartValue(menu_width)
        self.animation_left_menu.setEndValue(new_width)
        self.animation_left_menu.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation_left_menu.start()
    
    def cancel(self):
        
        self.app.running_thread = None
        self.app.has_legend = False
        self.app.ui.lbl_first_place_value.clear()
        self.app.ui.lbl_first_place_sum.clear()
        self.app.ui.lbl_second_place_value.clear()
        self.app.ui.lbl_second_place_sum.clear()
        self.app.ui.lbl_third_place_value.clear()
        self.app.ui.lbl_third_place_sum.clear()
        self.app.ui.tableWidget.setRowCount(0)
        self.app.ui.lbl_min_succeed_value.clear()
        self.app.ui.lbl_perfect_value.clear()
        self.app.ui.btn_cancel.setDisabled(True)
        self.app.ui.lbl_best_score_value.setText("0")
        self.app.ui.lbl_elapsed_time_value.setText("0")
        self.app.ui.lbl_gens_value.setText("0")
        self.app.ui.lbl_muts_value.setText("0")
        self.app.ui.lbl_worst_score_value.setText("0")
        self.info_plt_axes.clear()
        self.canvas.draw()
        self.app.ui.btn_start_restart.setText("Start")

    def placement(self, podium):
        _winners = podium[:3]
        _winners_lbl= [self.app.ui.lbl_first_place_value, self.app.ui.lbl_second_place_value,self.app.ui.lbl_third_place_value]
        _winners_sum= [self.app.ui.lbl_first_place_sum, self.app.ui.lbl_second_place_sum,self.app.ui.lbl_third_place_sum]
        for i, x in enumerate(_winners):
            _winners_lbl[i].setText("  " + str(x))
            _winners_sum[i].setText(str(sum(x)))

        self.app.ui.tableWidget.setRowCount(len(podium[len(_winners):])) 
        self.app.ui.tableWidget.setColumnCount(2) 
        self.app.ui.tableWidget.setColumnHidden(2,True) 
        self.app.ui.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.app.ui.tableWidget.horizontalHeader().setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        self.app.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
       
        for i, x in enumerate(podium[len(_winners):]):
            self.app.ui.tableWidget.setItem(i, 1, QTableWidgetItem((f"  { str(x)}  ")))
            self.app.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(sum(x))))
            self.app.ui.tableWidget.item(i,0).setTextAlignment(QtCore.Qt.AlignCenter)
      