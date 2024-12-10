##from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
##from Interface.qt_core import *

from ui_main_window import *

import sys
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        # Configurações principais da janela
        self.setWindowTitle("Produsys")
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Cria e exibe a janela principal
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
