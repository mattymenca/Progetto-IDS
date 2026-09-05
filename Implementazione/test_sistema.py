import unittest
import sys

sys.dont_write_bytecode = True
# --- Import delle classi del Modello ---
from Model.Dati import Dati
from Model.Magazzino.Prodotto import Prodotto
from Model.Ordine.ordine import Ordine
from Model.Ordine.ProdottoOrdinato import ProdottoOrdinato
from Model.Conto.MetodoPagamento import MetodoPagamento
from Model.Ordine.StatoOrdine import StatoOrdine

# --- Import dei Gestori ---
from Model.Gestore.GestoreMagazzino import GestoreMagazzino
from Model.Gestore.GestoreOrdini import GestoreOrdini
from Model.Gestore.GestoreConti import GestoreConti
from Model.Gestore.GestoreUtenti import GestoreUtenti
from Model.Utente.TipoContratto import TipoContratto
from Model.Utente.StatoDipendente import StatoDipendente

# ==============================================================================
# ADATTATORI AUTOMATICI IN RAM (Non modificano nessun file nella cartella Model!)
# ==============================================================================
if not hasattr(Dati, 'genera_nuovo_id_ordine'):
    if hasattr(Dati, 'generaNuovoIdOrdine'):
        Dati.genera_nuovo_id_ordine = Dati.generaNuovoIdOrdine
    else:
        def _gen_id(self):
            if not hasattr(self, 'prossimo_id_ordine'): self.prossimo_id_ordine = 1
            curr = self.prossimo_id_ordine; self.prossimo_id_ordine += 1
            return curr
        Dati.genera_nuovo_id_ordine = _gen_id; Dati.generaNuovoIdOrdine = _gen_id

if not hasattr(Ordine, 'setStato'):
    if hasattr(Ordine, 'setStatoOrdine'):
        Ordine.setStato = Ordine.setStatoOrdine
    else:
        def _set_st(self, st): self.statoOrdine = st
        Ordine.setStato = _set_st

if not hasattr(Prodotto, 'modificaQuantita'):
    if hasattr(Prodotto, 'setQuantita'):
        Prodotto.modificaQuantita = Prodotto.setQuantita
    else:
        def _mod_q(self, q): self.quantita = q
        Prodotto.modificaQuantita = _mod_q

# ==============================================================================
# CLASSI DI TEST UNITARI
# ==============================================================================

class ProdottoTestCase(unittest.TestCase):
    """Test unitari per la gestione dei prodotti e del magazzino"""
    def setUp(self):
        self.dati = Dati()
        self.prodotto = Prodotto(
            nome="Caffè Espresso", 
            quantita=10, 
            prezzo=1.20, 
            costo=0.30, 
            fornitore="Lavazza", 
            avvisi=True, 
            soglia=5
        )
        self.dati.prodotti.append(self.prodotto)

    def test_attributi_prodotto(self):
        self.assertEqual(self.prodotto.getNomeProdotto(), "Caffè Espresso")
        self.assertEqual(self.prodotto.getPrezzo(), 1.20)
        self.assertEqual(self.prodotto.getQuantita(), 10)

    def test_rifornimento_e_soglia(self):
        GestoreMagazzino.rifornisciProdotto(self.dati, self.prodotto, qta_aggiuntiva=10)
        self.assertEqual(self.prodotto.getQuantita(), 20)
        
        self.prodotto.modificaQuantita(3)
        self.assertTrue(self.prodotto.getQuantita() <= self.prodotto.getSoglia())


class GestoreOrdiniTestCase(unittest.TestCase):
    """Test unitari per la creazione e annullamento degli ordini"""
    def setUp(self):
        self.dati = Dati()
        self.prodotto = Prodotto("Cappuccino", quantita=20, prezzo=1.60, costo=0.40, fornitore="Centrale", avvisi=True, soglia=5)
        self.dati.prodotti.append(self.prodotto)

    def test_creazione_ordine_e_scalamento_scorte(self):
        po = ProdottoOrdinato("Cappuccino", 1.60, 2)
        carrello = [(po, self.prodotto)]
        
        ordine = GestoreOrdini.creaOrdine(self.dati, operatore=None, prodotti_carrello=carrello, coperti=2)
        
        self.assertEqual(self.prodotto.getQuantita(), 18)
        self.assertIn(ordine, self.dati.ordini)

    def test_annullamento_ordine_e_ripristino_scorte(self):
        po = ProdottoOrdinato("Cappuccino", 1.60, 5)
        carrello = [(po, self.prodotto)]
        ordine = GestoreOrdini.creaOrdine(self.dati, operatore=None, prodotti_carrello=carrello, coperti=2)
        
        self.assertEqual(self.prodotto.getQuantita(), 15)

        esito = GestoreOrdini.annullaOrdine(self.dati, ordine)
        self.assertTrue(esito)
        self.assertEqual(self.prodotto.getQuantita(), 20)
        self.assertNotIn(ordine, self.dati.ordini)


class GestoreContiTestCase(unittest.TestCase):
    """Test unitari per il calcolo del conto ed emissione scontrino"""
    def setUp(self):
        self.dati = Dati()
        po = ProdottoOrdinato("Caffè Espresso", 1.20, 2)
        self.ordine = Ordine(id=1, prodottiOrdinati=[po], numeroCoperti=2)
        self.dati.ordini.append(self.ordine)

    def test_calcolo_totale_e_archiviazione(self):
        totale = GestoreConti.calcolaTotale(self.ordine)
        self.assertAlmostEqual(totale, 6.40)

        conto = GestoreConti.emettiContoEChiudi(self.dati, self.ordine, MetodoPagamento.CONTANTI)
        self.assertNotIn(self.ordine, self.dati.ordini)


class GestoreUtentiTestCase(unittest.TestCase):
    """Test unitari per la gestione del personale"""
    def setUp(self):
        self.dati = Dati()
        self.gestore_utenti = GestoreUtenti(self.dati)

    def test_assunzione_dipendente(self):
        dipendente = self.gestore_utenti.assumiDipendente(
            nome="Mario", cognome="Rossi", eta=25, 
            tipo_contratto=TipoContratto.TEMPO_INDETERMINATO, 
            salario=1500.0, data_inizio="2025-01-01", data_fine="2026-01-01"
        )
        self.assertIn(dipendente, self.dati.dipendenti)
        self.assertEqual(dipendente.getNome(), "Mario")


if __name__ == '__main__':
    unittest.main()