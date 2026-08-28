# See readme.md for instructions on running this code.
from typing import Any, Dict
from zulip_bots.lib import AbstractBotHandler;
import zulip;

# Funciones creadas
from src.database.queries import find_ticket;

# Modelos creados
from src.models.impacto import Impacto;
from src.models.prioridad import Prioridad;
from src.models.urgencia import Urgencia;
from src.models.messages import Messages;

# Constantes creadas
from src.settings.settings import ZULIP_URL;

class SoporteHandler():
    def usage(self) -> str:
        return """
        Este bot es el encargado de brindar soporte técnico básico
        a los colcaboradores desde el chat directo con él,
        este bot después de hablar con el colaborador podrá informarle
        al personal de soporte técnico sobre la incidencia reportada.
        """

    def handle_message(self, message: Dict[str, Any], bot_handler: AbstractBotHandler) -> None:
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
        
        # Validacion de los comandos para el bot
        # Comando /Ayuda -> Comando principal para:
        # - Crear casos
        # - Validar el estado del caso y actualizaciones("posteriormente")
        #   - Obtener informacion del caso
        #   - Obtener informacion de soporte - contacto
        if bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["process"] == "/ayuda" or message["full_content"].lower() == "/ayuda":
            
            # Si el comando no esta inicializado
            if bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"] == None:
                content = "".join(map(str, Messages.MESSAGE_AYUDA_WELCOME.value));
                
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
                if message["full_content"].lower() == "/si":
                    bot_handler.send_reply(message, "".join(map(str, Messages.MESSAGE_AYUDA_TICKET_YES.value)));
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
                elif message["full_content"].lower() == "/no":
                    bot_handler.send_reply(message, "".join(map(str, Messages.MESSAGE_CASO_CHANELS.value)));
                    bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                            "name":message["sender_full_name"], 
                            "email":message["sender_email"],
                            "process":None, 
                            "step":None, 
                            "is_completed": False
                        }
                    )
                else :
                    bot_handler.send_reply(message, "Comando no válido, recuerda que las opciones validas son: ");

            # Si esta activo el proceso de 'caso'
            # Se pregunta al usuario si tiene el id del caso
            elif bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"] == "id_ticket":
                
                list_message = message["full_content"].split("/");
                print(list_message)
                if len(list_message) == 2 and list_message[0].lower() == "/":
                    
                    bot_handler.send_reply(message, "Se esta consultando el ticket");
                    info_ticket = find_ticket(int(list_message[1]));
                    print(info_ticket)
                    
                    # Si no encuentra ningun ticket con ese id
                    if (info_ticket == []):
                        bot_handler.send_reply(message, "Ticket no encontrado");
                    else:
                        
                        menssage_final = "".join(map(str, Messages.MESSAGE_INFO_TICKET.value))
                        menssage_final = menssage_final.replace("[ID_TICKET]", str(info_ticket[0][0]));
                        menssage_final = menssage_final.replace("[TITULO_TICKET]", info_ticket[0][1]);
                        menssage_final = menssage_final.replace("[PRIORIDAD]", str(info_ticket[0][3]));
                        menssage_final = menssage_final.replace("[CATEGORIA]", str(info_ticket[0][4]));
                        menssage_final = menssage_final.replace("[ENTIDAD]", info_ticket[0][5]);
                        menssage_final = menssage_final.replace("[SOLICITANTES]", info_ticket[0][6]);
                        menssage_final = menssage_final.replace("[CATEGORIA_TICKET]", info_ticket[0][7]);
                        menssage_final = menssage_final.replace("[TECNICOS]", info_ticket[0][9]);
                        
                        bot_handler.send_reply(message, "Ticket Consultado.");
                        bot_handler.send_reply(message,  menssage_final);
                        
                        bot_handler.send_message({
                            "type": "stream",
                            "to": "Soporte",
                            "subject": "Consulta de Soporte Técnico",
                            "content": f"`@**all** ` Hola compañeros, {message['sender_full_name']} acaba de consultar sobre su ticket, por favor alguno comuniquese con el colaborador para brindarle soporte.",
                        })
                        
                        content = "".join(map(str, Messages.MESSAGE_RUSDESK_OS.value));
                        bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                                "name":message["sender_full_name"], 
                                "email":message["sender_email"],
                                "process":"/rustdesk", 
                                "step":"os", 
                                "is_completed": False
                            }
                        );
                        bot_handler.send_reply(message, content);

                    # bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                    #         "name":None, 
                    #         "email":None,
                    #         "process":None, 
                    #         "step":None, 
                    #         "is_completed": None
                    #     }
                    # );
                else:
                    bot_handler.send_reply(message, "Comando no válido, recuerda que las opciones validas son: ");           
            
        # Comando /caso -> Comando principal para:
        # - Crear casos - Para versiones posteriores
        # - Ofrecer canales de comunicacion
        elif bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["process"] == "/caso" or message["full_content"].lower() == "/caso":
            print("Entramos al condicional de /caso")
            # Si el comando no esta inicializado
            if bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"] == None:
                # content = "".join(map(str, Messages.MESSAGE_CASO_WELCOME.value));
                status_dict = bot_handler.storage.get("status");
                bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                        "name":message["sender_full_name"], 
                        "email":message["sender_email"],
                        "process":"/caso", 
                        "step":"caso", 
                        "is_completed": False
                    }
                );
            content = "".join(map(str, Messages.MESSAGE_CASO_CHANELS.value));
            bot_handler.send_reply(message, content);
            bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                    "name":message["sender_full_name"], 
                    "email":message["sender_email"],
                    "process":None, 
                    "step":None, 
                    "is_completed": False
                }
            );

        
        # Comando /rustdesk -> Comando principal para:
        # - Verificar el codigo de rustdesk segun el os
        elif bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["process"] == "/rustdesk" or message["full_content"].lower() == "/rustdesk":
            
            # Si el comando no esta inicializado
            if bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"] == None:
                content = "".join(map(str, Messages.MESSAGE_RUSDESK_OS.value));
                bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                        "name":message["sender_full_name"], 
                        "email":message["sender_email"],
                        "process":"/rustdesk", 
                        "step":"os", 
                        "is_completed": False
                    }
                );
                bot_handler.send_reply(message, content);     
                   
            # Si esta activo el proceso de 'os'
            # Se pregunta al usuario si tiene un caso activo
            elif bot_handler.storage.get(f"{message['sender_full_name']}@aciel.co")["step"] == "os":

                # Si la respuesta es '/windows'
                # Se hace una petición a al api de zulip, se carga el archivo y se envia atachado
                if message["full_content"].lower() == "/windows":
                    
                    # Pass the path to your zuliprc file here.
                    client = zulip.Client(config_file="./zuliprc"); 
                    # Upload a file.
                    # 0 -> url bat
                    # 1 -> url image bat
                    list_files = []
                    with open("./src/scripts/code_rustdesk.bat", "rb") as fp:
                        result = client.upload_file(fp);
                        list_files.append(result["url"]);

                    with open("./src/media/code_rustdesk/windows.png", "rb") as fp:
                        result = client.upload_file(fp);
                        list_files.append(result["url"]);

                    content = "".join(map(str, Messages.MESSAGE_RUSDESK_URL_FILE.value));
                    content = content.replace("[URL_ARCHIVO]", list_files[0]);
                    image_url = ZULIP_URL + list_files[1];


                    bot_handler.send_reply(message, content);
                    bot_handler.send_reply(message, image_url);

                    bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                            "name":message["sender_full_name"], 
                            "email":message["sender_email"],
                            "process":None, 
                            "step":None, 
                            "is_completed": False
                        }
                    );
                # Si la respuesta es '/windows'
                # Se hace una petición a al api de zulip, se carga el archivo y se envia atachado
                elif message["full_content"].lower() == "/linux":
                    # Pass the path to your zuliprc file here.
                    client = zulip.Client(config_file="./zuliprc");

                    # Upload a file.
                    # 0 -> url bat
                    # 1 -> url image bat
                    list_files = []
                    with open("./src/scripts/code_rustdesk.sh", "rb") as fp:
                        result = client.upload_file(fp);
                        list_files.append(result["url"])
                        
                    with open("./src/media/code_rustdesk/windows.png", "rb") as fp:
                        result = client.upload_file(fp);
                        list_files.append(result["url"])
                        
                    content = "".join(map(str, Messages.MESSAGE_RUSDESK_URL_FILE.value));
                    content = content.replace("[URL_ARCHIVO]", list_files[0]);
                    image_url = ZULIP_URL + list_files[1];
                    
                     
                    bot_handler.send_reply(message, content);
                    bot_handler.send_reply(message, image_url);
                    
                    bot_handler.storage.put(f"{message['sender_full_name']}@aciel.co", {
                            "name":message["sender_full_name"], 
                            "email":message["sender_email"],
                            "process":None, 
                            "step":None, 
                            "is_completed": False
                        }
                    );
                else :
                    bot_handler.send_reply(message, "Comando no válido, recuerda que las opciones validas son: ");
        
        else:
            content = "".join(map(str, Messages.MESSAGE_GENERAL.value));
            content = content.replace("[NOMBRE_USUARIO]", message["sender_full_name"]);
            bot_handler.send_reply(message, content);


handler_class = SoporteHandler;