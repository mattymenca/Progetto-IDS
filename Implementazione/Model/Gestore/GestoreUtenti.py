from Model.Utente.Dipendente import Dipendente
from Model.Utente.Contratto import Contratto
from Model.Utente.StatoDipendente import StatoDipendente

class GestoreUtenti:
    def __init__(self, dati):
        self.dati = dati

    def validaCredenziali(self, nome, password):
        if not self.dati.manager:
            return False
        return (nome == self.dati.manager.getNome() and password == self.dati.manager.password)

    def assumiDipendente(self, nome, cognome, eta, tipo_contratto, salario, data_inizio, data_fine):
        contratto = Contratto(tipo_contratto, data_inizio, data_fine, salario)
        dipendente = Dipendente(nome, cognome, eta, [], [contratto], StatoDipendente.IMPIEGATO)
        self.dati.dipendenti.append(dipendente)
        self.dati.salvaTutto("dati.pkl")
        return dipendente

    def cambiaStatoDipendente(self, dipendente, nuovo_stato):
        dipendente.modificaStatoDipendente(nuovo_stato)
        self.dati.salvaTutto("dati.pkl")

    def modificaDatiDipendente(self, dipendente, column, valore_testo):
        """Modifica l'attributo specifico del dipendente o del suo contratto"""
        if column == 0: 
            dipendente.setNome(valore_testo)
        elif column == 1: 
            dipendente.setCognome(valore_testo)
        elif column == 2: 
            dipendente.setEta(int(valore_testo))
        elif column in [3, 4, 5, 6]:
            storico = dipendente.getStoricoContratti()
            if storico:
                c = storico[-1]
                if column == 4: 
                    c.modificaSalario(float(valore_testo))
                elif column == 5: 
                    c.setDataInizio(valore_testo)
                elif column == 6: 
                    c.setDataFine(valore_testo)

        self.dati.salvaTutto("dati.pkl")