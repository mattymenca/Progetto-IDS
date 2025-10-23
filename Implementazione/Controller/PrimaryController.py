from Model.GestoreUtenti import GestoreUtenti

# Controller/PrimaryController.py
from PyQt5.QtWidgets import QWidget, QMainWindow # Import necessario per i tipi

class PrimaryController:
    """
    Gestisce i riferimenti persistenti di tutti i Controller (schermate)
    e garantisce che ci sia una sola istanza di un dato tipo di Controller
    in un dato momento.
    """
    def __init__(self, dati):
        # Mappa per memorizzare i riferimenti: {NomeClasse: IstanzaController}
        self.active_controllers = {}
        
        # Riferimento al Controller attualmente visibile
        self.current_controller = None
        self.gestore_utenti = GestoreUtenti(dati)

    def mostraFinestra(self, ControllerClass, *args, **kwargs):
        """
        Nasconde la finestra attuale e mostra la finestra del controller specificato.
        Se un'istanza di quel ControllerClass esiste già, la riutilizza.
        Altrimenti, ne crea una nuova, passando 'self' (PrimaryController) come primo argomento.
        """
        
        # 1. INTERCETTA L'ARGOMENTO SPECIALE 'start_maximized' DA KWARGS
        # kwargs.pop('start_maximized', False) fa tre cose:
        #   - Cerca la chiave 'start_maximized' nel dizionario kwargs.
        #   - Se la trova, restituisce il suo valore (es. True) E LA RIMUOVE da kwargs.
        #   - Se non la trova, restituisce il valore di default (False) senza dare errore.
        start_maximized = kwargs.pop('start_maximized', False)
        controller_name = ControllerClass.__name__
        
        # 2. Verifica se l'istanza esiste già
        if controller_name in self.active_controllers:
            # Usa l'istanza esistente
            new_controller = self.active_controllers[controller_name]
        else:
            # 3. Crea una nuova istanza
            # Passa 'self' (PrimaryController) come primo argomento non-keyword
            # al costruttore del Controller specifico.
            new_controller = ControllerClass(self, *args, **kwargs)
            
            # 4. Salva il riferimento nel registro
            self.active_controllers[controller_name] = new_controller

        # 5. Gestisce la visibilità
        if self.current_controller is not None:
            # Nasconde la finestra attuale
            self.current_controller.hide()
            
        # 6. Aggiorna e mostra la nuova finestra
        self.current_controller = new_controller
        self.current_controller.show()
        
        # 7. APPLICA LO STATO ALLA NUOVA FINESTRA PRIMA DI MOSTRARLA
        # Usa la variabile che abbiamo catturato al punto 1.
        if start_maximized:
            self.current_controller.showMaximized()
        else:
            self.current_controller.show()

    def chiudiErimuovi(self, controller_instance):
        """
        Chiude e rimuove il riferimento a un controller, permettendo al GC di agire.
        Usato quando si chiude definitivamente una schermata.
        """
        controller_name = controller_instance.__class__.__name__
        
        if controller_name in self.active_controllers:
            # Rimuove il riferimento e chiude la finestra
            self.active_controllers.pop(controller_name)
            
            # Se è il controller corrente, lo resetta
            if self.current_controller == controller_instance:
                self.current_controller = None
                
            # Distrugge l'oggetto QWidget in modo pulito
            controller_instance.deleteLater()
