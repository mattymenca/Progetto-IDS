from Model.Gestore import Gestore, Dati
from Model.Magazzino.Magazzino import Magazzino
from Controller.Inits.Inizializza import Inits

if __name__ == "__main__":
    dati = Dati()
    dati.caricaDati("File")
    Inits.init()
    magazzino = Magazzino(dati.prodotti)
    Gestore.creaNuovoProdotto(magazzino, "mela", 5, 1, 0.5, "Tizio", False, 10)
