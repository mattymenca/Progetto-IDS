from Model.Gestore.GestoreOrdini import GestoreOrdini
from Model.Conto.Conto import Conto, MetodoPagamento
from Model.Ordine.ordine import Ordine
from Model.Dati import Dati

class GestoreConti:
    
    def __init__(self, dati: Dati, gestoreOrdini: GestoreOrdini):
        self.dati = dati
        self.gestoreOrdini = gestoreOrdini
        
    def creaConto(self, ordine: Ordine, metodoPagamento: MetodoPagamento):
        if ordine is not None:
            nuovoConto = Conto(ordine.getId(), metodoPagamento)
            nuovoConto.calcolaTotale(ordine)
        
            self.gestoreOrdini.concludiOrdine(ordine)
            self.dati.conti.append(nuovoConto)
            self.dati.setDirty()
        
            return True
        return False
    
 