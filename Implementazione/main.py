from Implementazione.Model.Dati import Gestore, Dati
from Model.Magazzino.Magazzino import Magazzino
from Controller.Inits.Inizializza import Finestra

if __name__ == "__main__":
    dati = Dati()
    dati.caricaDati("File")
    finestra = Finestra()
    magazzino = Magazzino(dati.prodotti)
    Gestore.creaNuovoProdotto(magazzino, "mela", 5, 1, 0.5, "Tizio", False, 10)
