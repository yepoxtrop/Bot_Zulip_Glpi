from enum import Enum
from textwrap import dedent

from src.settings.settings import (
    CORREO_SOPORTE,
    GLPI_URL,
    NUMERO_SOPORTE1,
    NUMERO_SOPORTE2,
)

class Messages(Enum):

    MESSAGE_AYUDA_WELCOME = dedent("""
        Hola, soy **Tech**, tu asistente de soporte técnico.
        Antes de continuar, recuerda que toda solicitud debe registrarse en **Helpdesk**, donde se genera un **ID de caso**.

        ¿Ya creaste tu caso en Helpdesk? Selecciona una opción:
        ✅ `1` → Sí, ya tengo un ID de caso.
        ❌ `2` → No, todavía no he creado el caso.
    """)

    MESSAGE_AYUDA_TICKET = dedent("""
        Perfecto. Para continuar, necesito el **ID de tu ticket**.

        Envíame únicamente el número del ticket.
        👉 Ejemplo: `4168`
    """)

    MESSAGE_AYUDA_TICKET_YES = dedent("""
        Por favor, envíame únicamente el número de tu ticket.
        👉 Ejemplo: `4168`
    """)

    MESSAGE_AYUDA_TICKET_NO = dedent("""
        Entiendo que aún no tienes un caso creado.

        ¿Deseas que te ayude a crear un nuevo ticket?

        ✅ `1` → Crear un nuevo ticket.
        ❌ `2` → Lo crearé más tarde.
    """)
    
    MESSAGE_INFO_TICKET = dedent("""
        📌 **Resumen de tu ticket**

        - **ID:** [ID_TICKET]
        - **Estado:** [ESTADO]
        - **Título:** [TITULO_TICKET]
        - **Urgencia:** [URGENCIA]
        - **Prioridad:** [PRIORIDAD]
        - **Entidad:** [ENTIDAD]
        - **Solicitante(s):** [SOLICITANTES]
        - **Categoría:** [CATEGORIA_TICKET]
        - **Técnico(s) asignado(s):** [TECNICOS]
    """)
    
    MESSAGE_CASO_WELCOME = dedent("""
        Hola, soy **Tech**, tu asistente de soporte técnico.
        Vamos a gestionar tu solicitud en **Helpdesk**, donde se genera un **ID de caso**.

        ¿Qué deseas hacer? Selecciona una opción:
        ✅ `1` → Consultar un ticket existente.
        ❌ `2` → Ver los canales para crear un ticket.
    """)
    
    MESSAGE_CASO_CHANELS = dedent(f"""
        Puedes registrar o consultar tus solicitudes a través de estos canales:
        💻 `GLPI`: {GLPI_URL}
        📱 `WHATSAPP CORPORATIVO 1`: {NUMERO_SOPORTE1}
        📱 `WHATSAPP CORPORATIVO 2`: {NUMERO_SOPORTE2}
        ✉️ `CORREO CORPORATIVO`: {CORREO_SOPORTE}

        🕒 **Horario de atención**

        - **Lunes a jueves:** 7:30 a. m. - 5:00 p. m.
        - **Viernes:** 7:30 a. m. - 4:30 p. m.
        - **Fines de semana y festivos:** No estamos disponibles.

        **DEPARTAMENTO DE TECNOLOGÍA - SOLUCIONES INTEGRALES**
    """)

    MESSAGE_RUSDESK_OS = dedent("""
        💻 ¿Qué sistema operativo utilizas? Así te enviaré el archivo correcto para obtener tu **ID de RustDesk**:

        `1` → Linux
        `2` → Windows 10 u 11

        Responde únicamente con `1` o `2`.
    """)

    MESSAGE_RUSDESK_URL_FILE = dedent("""
        ✅ Descarga el archivo desde este enlace:

        [URL_ARCHIVO]

        📋 Cuando lo ejecutes, se mostrará tu **ID de RustDesk**.
        El equipo de soporte podrá solicitarte ese ID para conectarse.
    """)

    MESSAGE_GENERAL = dedent("""
        👋 Hola [NOMBRE_USUARIO], un gusto saludarte.
        🤖 Soy **Tech**, tu asistente de soporte técnico de **Aciel Soluciones Integrales**.

        📋 ¿En qué puedo ayudarte?
        - `/Ayuda` → Consultar el estado de un ticket.
        - `/Caso` → Ver los canales para crear o consultar un ticket.
        - `/Rustdesk` → Obtener ayuda con tu ID de RustDesk.
    """)
    
    