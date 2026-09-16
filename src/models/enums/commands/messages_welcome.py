from enum import Enum;
from textwrap import dedent

class Welcome_Messages(Enum):
    
    WELCOME_GENERAL_MESSAGE = dedent("""
        👋 Hola [NOMBRE_USUARIO], un gusto saludarte.
        🤖 Soy **Tech**, tu asistente de soporte técnico de **Aciel Soluciones Integrales**.

        📋 ¿En qué puedo ayudarte?
        - `1` → Consultar el estado de un ticket.
        - `2` → Ver los canales para crear o consultar un ticket.
        - `3` → Obtener ayuda con tu ID de RustDesk.
        - `4` → Obtener ayuda general.
        - `5` → Calificar soporte técnico.
    """);
    
    WELCOME_CHANELS_GENERAL_MESSAGE = dedent("""
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
    """);
    
    WELCOME_ERROR_GENERAL_MESSAGE = dedent("""
        👋 Hola [NOMBRE_USUARIO], un gusto saludarte.
        En estos momentos presentamos problemas técnicos, por favor intenta más tarde.
    """);
    
    