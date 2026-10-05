from enum import Enum


class Request_Types(Enum):
    HELPDESK = [ 1, "Helpdesk"];
    E_MAIL = [ 2, "E-Mail"];
    PHONE = [ 3, "Phone"];
    DIRECT = [ 4, "Direct"];
    WRITTEN = [ 5, "Written"];
    OTHER = [ 6, "Other"];
    BOT_ZULIP = [ 7, "Bot zulip"];