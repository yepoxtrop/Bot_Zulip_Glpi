from enum import Enum

class Messages(Enum):

    MESSAGE_AYUDA_WELCOME = (
        "Hola, soy **Tech**, tu asistente de soporte técnico.\n\n",
        "Antes de continuar, recuerda que toda solicitud debe registrarse en **Helpdesk**, donde se genera un **ID de caso**.\n\n",
        "¿Ya creaste tu caso en Helpdesk? Selecciona una opción:\n\n",
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