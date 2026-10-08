from .output.interface_email import IEmail;
from .output.interface_helpdesk import IHelpDesk;
from .output.interface_logs import ILogs;
from .output.interface_own_database import IOwnDatabase;
from .output.interface_ticket import ITicket;

__all__ = [
    "IEmail",
    "IHelpDesk",
    "ILogs",
    "IOwnDatabase",
    "ITicket"
];