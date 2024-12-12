from qt_core import * 
from pages.ui_page import *

class UI_MainWindow(object):
    def setup_ui(self, parent):
         if not parent.objectName():
              parent.setObjectName("MainWindow")
         
         parent.resize(1200, 720)
         parent.setMinimumSize(960, 540)
         
         self.central_frame = QFrame()
         
         self.main_layout = QHBoxLayout(self.central_frame)
         self.main_layout.setContentsMargins(0,0,0,0)
         self.main_layout.setSpacing(0)
         
         self.left_menu = QFrame()
         self.left_menu.setStyleSheet("background-color: #44475a")
         self.left_menu.setMinimumWidth(50)
         self.left_menu.setMaximumWidth(50)
         
         
         self.content = QFrame()
         self.content.setStyleSheet("background-color: #282a36")
         
         self.content_layout =  QVBoxLayout(self.content)
         self.content_layout.setContentsMargins(0,0,0,0)
         self.content_layout.setSpacing(0)
         
         self.top_bar = QFrame()
         self.top_bar.setMinimumHeight(30)
         self.top_bar.setMaximumHeight(30)
         self.top_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
         self.top_bar_layout = QHBoxLayout(self.top_bar)
         self.top_bar_layout.setContentsMargins(10,0,10,0)
         
         self.top_bar_left = QLabel("Loja de ferramentas")
         
         self.top_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

         
         self.top_label_right =  QLabel("| PÁGINA INICIAL")
         self.top_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")
         
         self.top_bar_layout.addWidget(self.top_bar_left)
         self.top_bar_layout.addItem(self.top_spacer)
         self.top_bar_layout.addWidget(self.top_label_right)
     
         
         self.bt_bar = QFrame()
         self.bt_bar.setMinimumHeight(30)
         self.bt_bar.setMaximumHeight(30)
         self.bt_bar.setStyleSheet("background-color: #21232d; color: #6272a4")
         
         
         
         self.pages = QStackedWidget()
         self.pages.setStyleSheet("font-size: 12pt; color: #f8f8f2")
         
         
         self.ui_pages = JanelaPP()
         self.ui_pages.configure(self.pages)

         
         
         ##baixo
         self.bnt_layout = QHBoxLayout(self.bt_bar)
         self.bnt_layout.setContentsMargins(10,0,10,0)
         
         self.bnt_left = QLabel("Criado por: Smith Slayer")
         
         self.bnt_spacer = QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

         self.bnt_label_right =  QLabel("0 2024")
         self.bnt_label_right.setStyleSheet("font: 700 9pt 'Segoe UI'")
         
         self.bnt_layout.addWidget(self.bnt_left)
         self.bnt_layout.addItem(self.bnt_spacer)
         self.bnt_layout.addWidget(self.bnt_label_right)
         
         
         self.content_layout.addWidget(self.top_bar)
         self.content_layout.addWidget(self.pages)
         self.content_layout.addWidget(self.bt_bar)
         
         self.main_layout.addWidget(self.left_menu)
         self.main_layout.addWidget(self.content)
     
         
         parent.setCentralWidget(self.central_frame)