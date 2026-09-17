from .enums.tickets import Impacto, Prioridad, Urgencia, Categorias, TipoTickets;


class TicketsOptions:
    IMPACTO = Impacto;
    PRIORIDAD = Prioridad;
    URGENCIA = Urgencia;    
    CATEGORIAS = Categorias;
    TIPO_TICKETS = TipoTickets;

__all__ = [TicketsOptions];