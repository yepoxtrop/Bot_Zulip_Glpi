from .enums.tickets import Impacto, Prioridad, Urgencia, Categorias, TipoTickets, Entities, Request_Types;


class TicketsOptions:
    IMPACTO = Impacto;
    PRIORIDAD = Prioridad;
    URGENCIA = Urgencia;    
    CATEGORIAS = Categorias;
    TIPO_TICKETS = TipoTickets;
    ENTITIES = Entities;
    REQUEST_TYPES = Request_Types;

__all__ = [TicketsOptions];