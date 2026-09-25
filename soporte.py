# See readme.md for instructions on running this code.
from typing import Any, Dict
from zulip_bots.lib import AbstractBotHandler;
import zulip;

# Funciones creadas
#from src.infrastructure.repositories.databases.queries.queries import find_ticket;

# Modelos creados
#from src.models.enums import Impacto, Prioridad, Urgencia;
#from src.models.messages import Messages;

# Constantes creadas
from src.settings.settings import ZULIP_URL, DOMINIO_CORPORATIVO;

from src.application.use_cases import Welcome;

class SoporteHandler():
    
    def usage(self) -> str:
        return """
        Este bot es el encargado de brindar soporte técnico básico
        a los colcaboradores desde el chat directo con él,mysql
        este bot después de hablar con el colaborador podrá informarle
        al personal de soporte técnico sobre la incidencia reportada.
        """

    def handle_message(self, message: Dict[str, Any], bot_handler: AbstractBotHandler) -> None:
        try:
            print(message)
                    
            # Si no existe la llave, la crea
            if not bot_handler.storage.contains(f"{message['sender_full_name']}@{DOMINIO_CORPORATIVO}"):
    
                # Almacenamiento de clave de usuario nombre@DOMINIO_CORPORATIVO
                bot_handler.storage.put(
                    f"{message['sender_full_name']}@{DOMINIO_CORPORATIVO}", {
                        "name":message["sender_full_name"], 
                        "email":message["sender_email"],
                        "process": None, 
                        "step": None, 
                        "is_completed": None
                    }
                );
            
            # Validacion de los comandos para el bot
            # Comando /Ayuda -> Comando principal para:
            # - Crear casos
            # - Validar el estado del caso y actualizaciones("posteriormente")
            #   - Obtener informacion del caso
            #   - Obtener informacion de soporte - contacto
            
            welcome_conversation = Welcome(message["full_content"]);
            list_msg = welcome_conversation.send_message();
            bot_handler.storage.put(f"{message['sender_full_name']}@{DOMINIO_CORPORATIVO}", {
                        "name":message["sender_full_name"], 
                        "email":message["sender_email"],
                        "process":welcome_conversation.section, 
                        "step":welcome_conversation.step, 
                        "is_completed": False
                    }
                );

            for msg in list_msg:
                bot_handler.send_reply(message, msg);
                
        except Exception as error:
            print(f"Error procesando el mensaje: {error}")
            raise


handler_class = SoporteHandler;