# See readme.md for instructions on running this code.

from typing import Any, Dict
from zulip_bots.lib import AbstractBotHandler

# Funciones creadas
from database.queries import find_ticket;

class SoporteHandler():
    def usage(self) -> str:
        return """
        Este bot es el encargado de brindar soporte técnico básico
        a los colcaboradores desde el chat directo con él,
        este bot después de hablar con el colaborador podrá informarle
        al personal de soporte técnico sobre la incidencia reportada.
        """

    def handle_message(self, message: Dict[str, Any], bot_handler: AbstractBotHandler) -> None:
        # Tuplas con los mensajes
        message_ayuda_welcome = (
        	"💬 Hola! 😊 \n",
        	"Recuerda que toda solicitud debe diligenciarse por medio de Helpdesk 🖥️, donde se genera un ID de caso 🔢.",
        	"¿Ya realizaste este proceso? 🤔💭 \n",
        	"`/Si` -> Ya create un caso. \n"
        	"`/No` -> Aún no has creado el caso."
        )

        message_ayuda_caso = (
        	"Id  \n",
        	"Regalanos el id del ticket.",
        	"`/Si numero_ticket` -> Si tienes el ticket. \n"
        	"`/No` -> Si no tienes el id."
        )

        message_adyuda_caso_si = (
            "Dame el id de ticket de la siguiente forma:\n",
            "`/Si numero_ticket` -> Si tienes el ticket.\n", 
            "`/No` -> Si no cuentas con el ticket."
        )

        message_adyuda_caso_no = (
            "¿Quieres crear un caso?:\n",
            "`/Si` -> Si quieres crear un nuevo ticket.\n", 
            "`/No` -> No quieres crear un nuevo ticket. "
        )
        print(message)
        # Si no existe la llave, la crea
        if not bot_handler.storage.contains(f"{message['sender_full_name']}@aciel.co"):

            # Almacenamiento de clave de usuario nombre@aciel.co
            bot_handler.storage.put(
                f"{message['sender_full_name']}@aciel.co", {
                    "name":message["sender_full_name"], 
                    "email":message["sender_email"],
                    "process": None, 
                    "step": None, 
                    "is_completed": None
                }
            );
        print(bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"]);

        # Validacion de los comandos para el bot
        # Comando /Ayuda -> Comando principal para:
        # - Crear casos
        # - Validar el estado del caso y actualizaciones
        # - Obtener informacion del caso
        # - Obtener informacion de soporte - contacto
        if bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["process"] == "/ayuda" or message["full_content"] == "/ayuda":
            
            # Si el comando no esta inicializado
            if bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"] == None:
                content = "".join(map(str, message_ayuda_welcome));
                status_dict = bot_handler.storage.get("status");
                bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                        "name":message["sender_full_name"], 
                        "email":message["sender_email"],
                        "process":"/ayuda", 
                        "step":"caso", 
                        "is_completed": False
                    }
                );
                bot_handler.send_reply(message, content);
            
            # Si esta activo el proceso de 'caso'
            # Se pregunta al usuario si tiene un caso activo
            elif bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"] == "caso":

                # Si la respuesta es '/si', se le pregunta a la persona si tiene el id
                # Se cambia el step a 'id_ticket'
                if message["full_content"] == "/si":
                    bot_handler.send_reply(message, "".join(map(str, message_adyuda_caso_si)));
                    bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                            "name":message["sender_full_name"], 
                            "email":message["sender_email"],
                            "process":"/ayuda", 
                            "step":"id_ticket", 
                            "is_completed": False
                        }
                    );

                # Si la respuesta es '/no', se le pregunta si quiere crear un caso
                # Se cambia el step a 'crear_ticker'
                elif message["full_content"] == "/no":
                    bot_handler.send_reply(message, "".join(map(str, message_adyuda_caso_no)));
                    bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                            "name":message["sender_full_name"], 
                            "email":message["sender_email"],
                            "process":"/ayuda", 
                            "step":"crear_ticket", 
                            "is_completed": False
                        }
                    )
                else :
                    bot_handler.send_reply(message, "Comando no válido, recuerda que las opciones validas son: ");

            # Si esta activo el proceso de 'caso'
            # Se pregunta al usuario si tiene el id del caso
            elif bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"] == "id_ticket":
                
                list_message = message["full_content"].split(" ");
                if len(list_message) == 2 and list_message[0] == "/si":
                    bot_handler.send_reply(message, "Se esta consultando el ticket");
                    bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                            "name":None, 
                            "email":None,
                            "process":None, 
                            "step":None, 
                            "is_completed": None
                        }
                    );
                elif list_message[0] == "/no":
                    
                    # preguntar si quiere crear el caso
                    bot_handler.send_reply(message, "".join(map(str, message_adyuda_caso_no)));
                    bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                            "name":message["sender_full_name"], 
                            "email":message["sender_email"],
                            "process":"/ayuda", 
                            "step":"crear_ticket", 
                            "is_completed": False
                        }
                    )
                else:
                    bot_handler.send_reply(message, "Comando no válido, recuerda que las opciones validas son: ");           
        else:
            print(bot_handler.storage.get("status"));
            content = f"Hola {message['sender_full_name']} , soy **Tech**, el asistente de soporte técnico de **Aciel Soluciones Integrales**.\nMis funciones son las siguientes:\n`/Ayuda`->Solcitud de soporte técnico.";
            bot_handler.send_reply(message, content);


handler_class = SoporteHandler;

