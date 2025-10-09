import sys
from PyQt5.QtWidgets import QApplication
from Model.Dati import Dati
from Model.GestoreMagazzino import GestoreMagazzino
from Model.Magazzino.Magazzino import Magazzino
from Controller.MainController import MainController

if __name__ == "__main__":
    app = QApplication(sys.argv)
    dati = Dati()
    dati.caricaDati("File")

    controller = MainController()
    controller.show()

    sys.exit(app.exec_())
