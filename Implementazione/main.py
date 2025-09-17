
from Model.Gestore import Gestore, Dati
from Model.Magazzino.Magazzino import Magazzino

if __name__ == "__main__":
    dati = Dati()
    dati.caricaDati("File")
    magazzino = Magazzino(dati.prodotti)
    Gestore.creaNuovoProdotto(magazzino, "mela", 5, 1, 0.5, "Tizio", False, 10)
