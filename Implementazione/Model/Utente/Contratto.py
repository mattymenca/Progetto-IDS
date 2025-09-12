from .TipoContratto import TipoContratto

class Contratto:

    def __init__(self, tipoContratto: TipoContratto, dataInizio, dataFine, salario):
        self.tipoContratto = tipoContratto
        self.dataInizio = dataInizio
        self.dataFine = dataFine
        self.salario = salario

    def getTipoContratto(self):
        return self.tipoContratto
    
    def getDataInizio(self):
        return self.dataInizio
    
    def getDataFine(self):
        return self.dataFine
    
    def getSalario(self):
        return self.salario
    
    def modificaTipoContratto(self, tipoContratto: TipoContratto):
        self.tipoContratto = tipoContratto

    def setDataInizio(self, dataInizio):
        self.dataInizio = dataInizio

    def setDataFine(self, dataFine):
        self.dataFine = dataFine

    def modificaSalario(self, salario: float):
        self.salario = salario