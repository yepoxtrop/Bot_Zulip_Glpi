from .enums.commands import (
    Docs_Messages,
    General_Messages,
    Help_Messages,
    Rate_Us_Messages,
    Rustdesk_Messages,
    Tickets_Messages,
    Welcome_Messages,
)

class Messages:
    DOCS_MESSAGES = Docs_Messages;
    GENERAL_MESSAGES = General_Messages;
    HELP_MESSAGES = Help_Messages;
    RATE_US_MESSAGES = Rate_Us_Messages;
    RUSTDESK_MESSAGES = Rustdesk_Messages;
    TICKETS_MESSAGES = Tickets_Messages;
    WELCOME_MESSAGES = Welcome_Messages,;
    
__all__ = [Messages];