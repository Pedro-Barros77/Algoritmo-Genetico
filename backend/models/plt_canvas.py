from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class plt_canvas(FigureCanvasQTAgg):
    """A canvas for graphics plotting
    """
    def __init__(self, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super(plt_canvas, self).__init__(fig)