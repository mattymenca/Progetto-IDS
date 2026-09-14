from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        
        # Set a modern, dark stylesheet
        MainWindow.setStyleSheet("""
            QMainWindow {
                background-color: #2c3e50;
            }
            QPushButton {
                background-color: #3498db;
                color: white;
                border: none;
                padding: 15px 30px;
                text-align: center;
                text-decoration: none;
                font-size: 16px;
                margin: 4px 2px;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #2980b9;
            }

            QMessageBox { background-color: #2c3e50; }
            QMessageBox QLabel { color: #ffffff; font-size: 14px; }
            QMessageBox QPushButton { 
                background-color: #34495e; 
                color: white; 
                border: 1px solid #7f8c8d; 
                border-radius: 4px; 
                padding: 6px 12px; 
            }
            QMessageBox QPushButton:hover { background-color: #2980b9; }
        """)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        # Use a central layout to arrange the buttons
        self.centralLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.centralLayout.setObjectName("centralLayout")
        self.centralLayout.setContentsMargins(50, 50, 50, 50)
        self.centralLayout.setSpacing(20)

        # Grid layout for the buttons
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setSpacing(20)

        self.pushButton_3 = QtWidgets.QPushButton("Dipendenti", self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_1")
        self.pushButton_3.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.pushButton_3, 1, 0, 1, 1)

        self.pushButton_4 = QtWidgets.QPushButton("Manager", self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_2")
        self.pushButton_4.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.pushButton_4, 1, 1, 1, 1)

        self.centralLayout.addLayout(self.gridLayout)
        
        MainWindow.setCentralWidget(self.centralwidget)
        
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Gestionale"))