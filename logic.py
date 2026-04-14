from PyQt6.QtWidgets import *
from final.gui import *


#ID must be made of 8 numbers

class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

