
from Model import Gestore
from Model.Magazzino.Magazzino import Magazzino


def main():
    dati = Gestore.Dati()
    dati.caricaDati()
    magazzino = Magazzino(dati.prodotti)
    Gestore.creaNuovoProdotto(magazzino, "mela", 5, 1, 0.5, "Tizio", False, 10)
    
    print(magazzino.prodottoDaInventario("mela").getNome())

if __name__ == "__main__":
    main()