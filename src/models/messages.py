from enum import Enum
from settings.settings import GLPI_URL, NUMERO_SOPORTE1, NUMERO_SOPORTE2, CORREO_SOPORTE;

class Messages(Enum):

    MESSAGE_AYUDA_WELCOME = (
        "Hola, soy **Tech**, tu asistente de soporte técnico.\n",
        "Antes de continuar, recuerda que toda solicitud debe registrarse en **Helpdesk**, donde se genera un **ID de caso**.\n\n",
        "¿Ya creaste tu caso en Helpdesk? Selecciona una opción:\n",
        "✅ `/Si` → Ya tengo un ID de caso.\n",
        "❌ `/No` → Aún no he creado el caso."
    )

    MESSAGE_AYUDA_TICKET = (
        "Perfecto. Para continuar, necesito el **ID de tu ticket**.\n\n",
        "Por favor, envíalo con el siguiente formato:\n",
        "👉 `/Si <numero_ticket>` (ejemplo: `/Si 4168`)\n\n",
        "Si no tienes el ID disponible, escribe:\n",
        "👉 `/No`"
    )

    MESSAGE_AYUDA_TICKET_YES = (
        "Por favor, envíame el ID del ticket con el siguiente formato:\n",
        "👉 `/Si <numero_ticket>` (ejemplo: `/Si 4168`)\n\n",
        "Si no cuentas con el ID en este momento, escribe:\n",
        "👉 `/No`"
    )

    MESSAGE_AYUDA_TICKET_NO = (
        "Entiendo que aún no tienes un caso creado.\n\n",
        "¿Deseas que te ayude a crear un nuevo ticket?\n\n",
        "✅ `/Si` → Crear un nuevo ticket.\n",
        "❌ `/No` → Lo crearé más tarde."
    )
    
    MESSAGE_INFO_TICKET = (
        "- `Id Ticket:` [ID_TICKET] \n",
        "- `Titulo Ticket:` [TITULO_TICKET] \n",
        # "- `Impacto:` \n", # - Informacion que trae la consulta, pero no tan relevante para el usuario
        "- `Prioridad:` [PRIORIDAD] \n",
        "- `Categoria:` [CATEGORIA] \n",
        "- `Entidad:` [ENTIDAD] \n",
        "- `Solicitantes:` [SOLICITANTES] \n",
        "- `Categoría Ticket:` [CATEGORIA_TICKET] \n",
        # "- `Id Técnicos:`", # - Informacion que trae la consulta, pero no tan relevante para el usuario
        "- `Técnicos:` [TECNICOS] \n"
    )
    
    MESSAGE_CASO_WELCOME = (
        "Hola, soy **Tech**, tu asistente de soporte técnico.\n",
        "Vamos a crear un caso en el **Helpdesk**, donde se genera un **ID de caso**.\n\n",
        "¿Quieres crear tu caso en Helpdesk? Selecciona una opción:\n",
        "✅ `/Si` → Ya tengo un ID de caso.\n",
        "❌ `/No` → Aún no he creado el caso."
    )
    
    MESSAGE_CASO_CHANELS = (
        "📋 Puedes registrar o consultar tus solicitudes a través de los siguientes canales:\n",
        f"💻 `GLPI`: {GLPI_URL}\n",
        f"📱 `WHATSAPP CORPORATIVO 1`: {NUMERO_SOPORTE1}\n",
        f"📱 `WHATSAPP CORPORATIVO 2`: {NUMERO_SOPORTE1}\n",
        f"✉️ `CORREO CORPORATIVO`: {CORREO_SOPORTE}\n\n",
        f"🕒 HORARIOS DE ATENCION\n\n",
        "SLOGAN"
    )

    MESSAGE_RUSDESK_OS = (
        "💻 Indícame cuál es tu sistema operativo para ayudarte a obtener tu **ID de RustDesk**:\n\n"
        "- `/Linux` → Si utilizas una distribución Linux.\n"
        "- `/Windows` → Si utilizas Windows 10 o Windows 11.\n"
    )

    MESSAGE_RUSDESK_URL_FILE = (
        "💻 Haz clic en el siguiente enlace para descargar el ejecutable:\n\n"
        "- [URL_ARCHIVO]\n\n"
        "📋 Una vez ejecutado, se mostrará tu **ID de RustDesk**.\n"
        "Puedes guiarte con la siguiente imagen de referencia:\n"
        #"[URL_IMAGEN]\n\n"
        #"✅ Cuando tengas el código, envíamelo con el siguiente formato:\n"
        #"👉 `/codigo <numero_codigo>`\n"
        #"Ejemplo: `/codigo 198580064`\n\n",
        #"En la pantalla verás un bloc de notas con un código, dime ese código de la siguiente manera:\n",
        #"👉 `/codigo <numero_codigo>` (ejemplo: `/codigo 198580064`)\n\n",
    )

    MESSAGE_GENERAL = (
        "👋 Hola [NOMBRE_USUARIO], un gusto saludarte.\n",
        "🤖 Soy **Tech**, tu asistente de soporte técnico de **Aciel Soluciones Integrales**.\n\n",
        "📋 Estas son las opciones disponibles:\n",
        "- `/Ayuda` → Solicitar soporte técnico.\n",
        "- `/Caso` → Obtener los enlaces para la creación de casos.\n",
        "- `/Rustdesk` → Consultar tu ID de RustDesk.\n",
        #"- `/Sys` → Solicitud de soporte técnico.\n", # -- Veriones futuras
        #"- `/Enlaces` → Solicitud de documentos para la mesa de ayuda.\n", # -- Veriones futuras
        #"- `/Caso` → Creacion de caso en glpi.\n", # -- Veriones futuras
    )