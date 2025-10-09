import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget

# Import your View classes and Model/Manager classes
from Controller.Inizializza import InizioView
# from View.magazzino import MagazzinoView  <-- You would create this for the Magazzino screen
# from Model.GestoreMagazzino import GestoreMagazzino 

class MainController(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # 1. Initialize the QStackedWidget as the central widget
        self.stack = QStackedWidget()
        self.setCentralWidget(self.stack)
        
        # 2. Initialize Model Managers (Data/Business Logic)
        # self.magazzino_manager = GestoreMagazzino()

        # 3. Initialize Views (UI Screens)
        self.inizio_view = InizioView()
        # self.magazzino_view = MagazzinoView()

        # 4. Add all views to the stack (the index matters)
        self.stack.addWidget(self.inizio_view)      # Index 0
        # self.stack.addWidget(self.magazzino_view)  # Index 1
        
        # 5. Connect Signals (User Actions) to Controller Slots (Logic)
        self.connect_signals()
        
        # Start by showing the initial view
        self.stack.setCurrentIndex(0)
        self.setWindowTitle("Main Application")

    def connect_signals(self):
        # Connect the buttons from the InizioView (index 0) to controller methods
        self.inizio_view.pushButton.clicked.connect(self.show_magazzino_view)
        self.inizio_view.pushButton_2.clicked.connect(self.show_tavoli_view)
        # ... connect other buttons (pushButton_3, pushButton_4)

    # Controller Methods (Slots)
    def show_magazzino_view(self):
        # Logic to switch to the Magazzino screen (Index 1)
        # self.stack.setCurrentIndex(1)
        print("Switching to Magazzino View...")

    def show_tavoli_view(self):
        # Logic to switch to the Tavoli screen
        print("Switching to Tavoli View...")

