from enum import Enum;
from textwrap import dedent

def Welcome_Messages(Enum):
    
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
    
    WELCOME_ERROR_GENERAL_MESSAGE = dedent("""
        👋 Hola [NOMBRE_USUARIO], un gusto saludarte.
        En estos momentos presentamos problemas técnicos, por favor intenta más tarde.
    """);