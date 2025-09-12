from .Ordine.StatoOrdine import StatoOrdine
from .Ordine.ordine import Ordine
from .Magazzino.Magazzino import Magazzino
from .Magazzino.Prodotto import Prodotto
import pickle
from .Conto.Conto import Conto
from .Conto.MetodoPagamento import MetodoPagamento
from .Magazzino.StatoProdotto import StatoProdotto
from .Utente.Contratto import Contratto
from .Utente.Dipendente import Dipendente
from .Utente.Manager import Manager
class Dati:
    def __init__(self):
        self.ordini = []
        self.contratti = []
        self.dipendenti = []
        self.prodotti = []
        self.manager = None
        
    def salvaTutto(self, nomeFile):
        try:
            with open(nomeFile, "wb") as file:
                pickle.dump(self, file)
        except (IOError, pickle.PicklingError) as e:
            print(f"Errore nel salvataggio dei dati: {e}")
        pass
    
    def caricaDati(self, nomeFile):
        try:
            with open(nomeFile, "rb") as file:
                dati = pickle.load(file)
        except (IOError, pickle.UnpicklingError) as e:
            print(f"Errore nel caricamento dei dati: {e}")
            
class Gestore:
    @staticmethod
    def approvaOrdine(ordine: Ordine, magazzino: Magazzino) -> bool:
        for prodottoOrdinato in ordine.getProdottiOrdinati():
            nomeProdotto = prodottoOrdinato.getNome()
            if prodottoOrdinato.getQuantita() > magazzino.prodottoDaInventario(nomeProdotto).getQuantita():
                Gestore.impostaStatoOrdine("non approvato")
                print("Ordine non approvato\n")
                return False
        Gestore.impostaStatoOrdine("in corso")
        print("Ordine in corso\n")
        return True
    
    # @staticmethod
    # def valida_ordine(ordine: Ordine, magazzino: Magazzino) -> bool:
    #     return all(
    #         p.getQuantita() <= magazzino.prodottoDaInventario(p.getNome()).getQuantita()
    #         for p in ordine.getProdottiOrdinati()
    #     )

    def impostaStatoOrdine(ordine: Ordine, stato: StatoOrdine):
        ordine.setStato(stato)
    
    @staticmethod
    def concludiOrdine(ordine: Ordine, dati: Dati):
        Gestore.impostaStatoOrdine("concluso")
        dati.ordini.append(ordine)
    
    @staticmethod
    def restituisciOrdine(idOrdine, ordini: list[Ordine]) -> Ordine:
        for ordine in ordini:
            if idOrdine == ordine.getId():
                return ordine
    
    @staticmethod
    def eliminaOrdine(idOrdine: int, ordini: list[Ordine]):
        for ordine in ordini:
            if idOrdine == ordine.getId:
                ordini.remove(ordine)    
    
    @staticmethod     
    def creaConto(ordine: Ordine, metodoPagamento: MetodoPagamento) -> Conto:
        nuovoConto = Conto(ordine.getId(), metodoPagamento)
        nuovoConto.calcolaTotale()
        Gestore.concludiOrdine(ordine)
        return nuovoConto
    
    @staticmethod
    def creaNuovoProdotto(magazzino: Magazzino, nome, quantita, prezzo, costo, fornitore, avvisi, soglia):
        nuovoProdotto = Prodotto(nome, quantita, prezzo, costo, fornitore, avvisi, soglia)
        magazzino.aggiungiProdotto(nuovoProdotto)
    
    @staticmethod
    def modificaStatoProdotto(prodotto: Prodotto, statoProdotto: StatoProdotto):
        prodotto.setStatoProdotto(statoProdotto)
        
    @staticmethod
    def eliminaProdotto(nomeProdotto: str, magazzino: Magazzino):
        inventario = magazzino.getInventario()
        for prodotto in magazzino.inventario:
            if nomeProdotto == prodotto.getNome():
                inventario.remove(prodotto)
                return True
        return False
        
    @staticmethod
    def aggiungiContratto(contratto: Contratto, dati: Dati):
        dati.contratti.append(contratto)
    
    @staticmethod
    def aggiungiDipendente(dipendente: Dipendente, dati: Dati): 
        dati.dipendenti.append(dipendente)
    
    @staticmethod
    def eliminaContratto(contratto: Contratto, dati: Dati):
        if contratto in dati.contratti:
            dati.contratti.remove(contratto)
            return True
        return False
    
    @staticmethod
    def eliminaDipendente(dipendente: Dipendente, dati: Dati):
        if dipendente in dati.dipendenti:
            dati.dipendenti.remove(dipendente)
            return True
        return False
    
    @staticmethod
    def cambiaManager(manager: Manager, dati: Dati):
        if not dati.manager is manager:
            dati.manager = manager
    
    @staticmethod
    def validaCredenziali(nome, password, dati: Dati):
        if nome != dati.manager.nome or password != dati.manager.password:
            print("Credenziali errate\n")
            return False
        return True
    
    @staticmethod
    def modificaCredenziali(nome, password, nuovaPassword, dati: Dati):
        if Gestore.validaCredenziali(nome, password) == False:
            print("Reinserire nome e password")
            return False
        
        dati.manager.password = nuovaPassword
        print("password modificata")
        return True
    
    
