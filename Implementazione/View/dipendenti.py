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

        self.pushButton_magazzino = QtWidgets.QPushButton("Magazzino", self.centralwidget)
        self.pushButton_magazzino.setObjectName("pushButton_magazzino")
        self.pushButton_magazzino.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.pushButton_magazzino, 0, 0, 1, 1)

        self.pushButton_conti = QtWidgets.QPushButton("Conti", self.centralwidget)
        self.pushButton_conti.setObjectName("pushButton_conti")
        self.pushButton_conti.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.pushButton_conti, 0, 1, 1, 1)

        self.pushButton_ordini = QtWidgets.QPushButton("Ordini", self.centralwidget)
        self.pushButton_ordini.setObjectName("pushButton_ordini")
        self.pushButton_ordini.setMinimumSize(QtCore.QSize(150, 50))
        self.gridLayout.addWidget(self.pushButton_ordini, 0, 2, 1, 1)

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
