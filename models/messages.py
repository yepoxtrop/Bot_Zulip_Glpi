from enum import Enum;

class Messages(Enum):
    MESSAGE_AYUDA_WELCOME = (
        "👋 ¡Hola! Soy **Tech**, tu asistente de soporte técnico. 🤖\n\n",
        "📋 Antes de continuar, recuerda que toda solicitud debe registrarse en **Helpdesk** 🖥️, donde se genera un **ID de caso** 🔢.\n\n",
        "🤔 ¿Ya creaste tu caso en Helpdesk? Selecciona una opción:\n\n",
        "✅ `/Si` → Ya tengo un ID de caso.\n",
        "❌ `/No` → Aún no he creado el caso."
    )
    
    MESSAGE_AYUDA_TICKET = (
        "🔍 ¡Perfecto! Para continuar necesito el **ID de tu ticket**.\n\n",
        "📝 Por favor, envíamelo con el siguiente formato:\n",
        "👉 `/Si <numero_ticket>` (ejemplo: `/Si 4168`)\n\n",
        "❓ ¿No tienes el ID a la mano?\n",
        "👉 Escribe `/No` para continuar sin él."
    )
    
    MESSAGE_AYUDA_TICKET_YES = (
        "⚠️ No entendí el formato de tu mensaje.\n\n",
        "📝 Por favor, envíame el ID con este formato:\n",
        "👉 `/Si <numero_ticket>` (ejemplo: `/Si 4168`)\n\n",
        "❓ ¿No tienes el ID?\n",
        "👉 Escribe `/No` para continuar sin él."
    )
    
    MESSAGE_AYUDA_TICKET_NO = (
        "🆘 Entiendo, aún no tienes un caso creado.\n\n",
        "💡 ¿Deseas que te ayude a crear uno nuevo ahora?\n\n",
        "✅ `/Si` → Sí, quiero crear un nuevo ticket.\n",
        "❌ `/No` → No, prefiero hacerlo después."
    )