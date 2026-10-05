from enum import Enum;
from textwrap import dedent

class Tickets_Messages(Enum):
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
    