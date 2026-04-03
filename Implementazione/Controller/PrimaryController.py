from Model.Gestore.GestoreUtenti import GestoreUtenti

# Controller/PrimaryController.py
from PyQt5.QtWidgets import QMessageBox # Import necessario per i tipi
from PyQt5.QtCore import Qt
class PrimaryController:
    """
    Gestisce i riferimenti persistenti di tutti i Controller (schermate)
    e garantisce che ci sia una sola istanza di un dato tipo di Controller
    in un dato momento.
    """
    def __init__(self, gestore_utenti: GestoreUtenti):
        # Mappa per memorizzare i riferimenti: {NomeClasse: IstanzaController}
        self.active_controllers = {}
        
        # Riferimento al Controller attualmente visibile
        self.current_controller = None
        self.gestore_utenti = gestore_utenti

    def mostra_finestra(self, ControllerClass, *args, **kwargs):
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

        # 5. Gestisce la visibilità della finestra precedente
        if self.current_controller is not None:
            # Salviamo se la finestra era ingrandita prima di nasconderla
            was_maximized = self.current_controller.isMaximized()
            self.current_controller.hide()
        else:
            was_maximized = False

        # 6. Aggiorna e prepara la nuova finestra
        self.current_controller = new_controller
        
        # 7. APPLICA LO STATO ALLA NUOVA FINESTRA
        if was_maximized or start_maximized:
            self.current_controller.setWindowState(self.current_controller.windowState() | Qt.WindowMaximized)
            self.current_controller.show()
        else:
            self.current_controller.show()
    def chiudi_e_rimuovi(self, controller_instance):
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
            
    def chiusura_sicura(self):
        
        # Metodo centralizzato per spegnere l'applicazione salvando i dati.
        # 1. Chiamiamo il logout/salvataggio nel Model
        successo = self.gestore_utenti.logout(path = "dati.pickle")
        
        if not successo:
            QMessageBox.critical(
                None, 
                "Errore di Salvataggio", 
                "Non è stato possibile salvare i dati su 'dati.pickle'.\n"
            )            
        # 2. Chiudiamo tutte le finestre attive nel registro
        for controller in list(self.active_controllers.values()):
            controller.close()
            
