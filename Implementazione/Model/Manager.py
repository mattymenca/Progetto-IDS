from Persona import Persona
class Manager(Persona):
    def __init__(self, nome, cognome, eta, ordini, password: str):
        super().__init__(nome, cognome, eta, ordini)
        self.password = password

