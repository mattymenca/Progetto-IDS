import sys
# Disattiva creazione __pycache__
sys.dont_write_bytecode = True

import unittest

# --- Import delle classi del Modello ---
from Model.Dati import Dati
from Model.Magazzino.Prodotto import Prodotto
from Model.Ordine.ordine import Ordine
from Model.Ordine.ProdottoOrdinato import ProdottoOrdinato
from Model.Conto.MetodoPagamento import MetodoPagamento

# --- Import dei Gestori ---
from Model.Gestore.GestoreMagazzino import GestoreMagazzino
from Model.Gestore.GestoreOrdini import GestoreOrdini
from Model.Gestore.GestoreConti import GestoreConti
from Model.Gestore.GestoreUtenti import GestoreUtenti
from Model.Utente.TipoContratto import TipoContratto

# ==============================================================================
# BLOCCO ASSOLUTO SALVATAGGI SU DISCO DURANTE I TEST
# ==============================================================================
Dati.salvaTutto = lambda self, nomeFile=None: None
Dati.caricaDati = lambda self, nomeFile=None: None

# ==============================================================================
# CLASSI DI TEST UNITARI
# ==============================================================================

class ProdottoTestCase(unittest.TestCase):
    def setUp(self):
        self.dati = Dati()
        self.gestore_magazzino = GestoreMagazzino(self.dati)
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
        # DELEGA AD ISTANZA GESTORE MAGAZZINO
        self.gestore_magazzino.rifornisciProdotto(self.prodotto, qta_aggiuntiva=10)
        self.assertEqual(self.prodotto.getQuantita(), 20)
        
        self.prodotto.setQuantita(3)
        self.assertTrue(self.prodotto.getQuantita() <= self.prodotto.getSoglia())


class GestoreOrdiniTestCase(unittest.TestCase):
    def setUp(self):
        self.dati = Dati()
        self.gestore_ordini = GestoreOrdini(self.dati)
        self.prodotto = Prodotto("Cappuccino", quantita=20, prezzo=1.60, costo=0.40, fornitore="Centrale", avvisi=True, soglia=5)
        self.dati.prodotti.append(self.prodotto)

    def test_creazione_ordine_e_scalamento_scorte(self):
        po = ProdottoOrdinato("Cappuccino", 1.60, 2)
        carrello = [(po, self.prodotto)]
        
        # DELEGA AD ISTANZA GESTORE ORDINI
        ordine = self.gestore_ordini.creaOrdine(persona=None, prodotti_carrello=carrello, coperti=2)
        
        self.assertEqual(self.prodotto.getQuantita(), 18)
        self.assertIn(ordine, self.dati.ordini)

    def test_annullamento_ordine_e_ripristino_scorte(self):
        po = ProdottoOrdinato("Cappuccino", 1.60, 5)
        carrello = [(po, self.prodotto)]
        ordine = self.gestore_ordini.creaOrdine(persona=None, prodotti_carrello=carrello, coperti=2)
        
        self.assertEqual(self.prodotto.getQuantita(), 15)

        # DELEGA AD ISTANZA GESTORE ORDINI
        esito = self.gestore_ordini.annullaOrdine(ordine)
        self.assertTrue(esito)
        self.assertEqual(self.prodotto.getQuantita(), 20)
        self.assertNotIn(ordine, self.dati.ordini)


class GestoreContiTestCase(unittest.TestCase):
    def setUp(self):
        self.dati = Dati()
        self.gestore_conti = GestoreConti(self.dati)
        po = ProdottoOrdinato("Caffè Espresso", 1.20, 2)
        self.ordine = Ordine(id=1, prodottiOrdinati=[po], numeroCoperti=2)
        self.dati.ordini.append(self.ordine)

    def test_calcolo_totale_e_archiviazione(self):
        # DELEGA AD ISTANZA GESTORE CONTI
        totale = self.gestore_conti.calcolaTotale(self.ordine)
        self.assertAlmostEqual(totale, 6.40)

        conto = self.gestore_conti.emettiContoEChiudi(self.ordine, MetodoPagamento.CONTANTI)
        self.assertNotIn(self.ordine, self.dati.ordini)


class GestoreUtentiTestCase(unittest.TestCase):
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