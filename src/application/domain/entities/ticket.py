import datetime


class Ticket:
    def __init__(
        self,
        id: int,
        entities_id: int,
        title_ticket: str,
        request_types: int,
        content: str,
        urgency: int,
        priority: int,
        impact: int,
        categories_id: int,
        type: int,
        slas_id_ttr: int,
        slas_id_tto: int,
        time_to_resolve: datetime.datetime,
        time_to_own: datetime.datetime,
        name_user: str,
        date_ticket: datetime.datetime | None = None,
    ):
        self.__id = id
        self._entities_id = entities_id
        self._title_ticket = title_ticket
        self._date_ticket = (
            date_ticket if date_ticket is not None else datetime.datetime.now()
        )
        self._request_types = request_types
        self._content = content
        self._urgency = urgency
        self._impact = impact
        self._priority = priority
        self._categories_id = categories_id
        self._type = type
        self._slas_id_ttr = slas_id_ttr
        self._slas_id_tto = slas_id_tto
        self._time_to_resolve = time_to_resolve
        self._time_to_own = time_to_own
        self._name_user = name_user

        self.validate()

    @property
    def id(self) -> int:
        return self.__id

    @property
    def entities_id(self) -> int:
        return self._entities_id

    @property
    def title_ticket(self) -> str:
        return self._title_ticket

    @property
    def date_ticket(self) -> datetime.datetime:
        return self._date_ticket

    @property
    def request_types(self) -> int:
        return self._request_types

    @property
    def content(self) -> str:
        return self._content

    @property
    def urgency(self) -> int:
        return self._urgency

    @property
    def impact(self) -> int:
        return self._impact

    @property
    def priority(self) -> int:
        return self._priority

    @property
    def categories_id(self) -> int:
        return self._categories_id

    @property
    def type(self) -> int:
        return self._type

    @property
    def slas_id_ttr(self) -> int:
        return self._slas_id_ttr

    @property
    def slas_id_tto(self) -> int:
        return self._slas_id_tto

    @property
    def time_to_resolve(self) -> datetime.datetime:
        return self._time_to_resolve

    @property
    def time_to_own(self) -> datetime.datetime:
        return self._time_to_own

    @property
    def name_user(self) -> str:
        return self._name_user

    def validate_id(self) -> bool:
        if not isinstance(self.__id, int) or isinstance(self.__id, bool):
            raise ValueError("Ticket id must be an integer.")
        return True

    def validate_entities_id(self) -> bool:
        if not isinstance(self._entities_id, int) or isinstance(self._entities_id, bool):
            raise ValueError("Entity id must be an integer.")
        return True

    def validate_title_ticket(self) -> bool:
        if not isinstance(self._title_ticket, str) or not self._title_ticket.strip():
            raise ValueError("Ticket title cannot be empty.")
        return True

    def validate_date_ticket(self) -> bool:
        if not isinstance(self._date_ticket, datetime.datetime):
            raise ValueError("Ticket date must be a datetime.")
        return True

    def validate_request_types(self) -> bool:
        if not isinstance(self._request_types, int) or isinstance(self._request_types, bool):
            raise ValueError("Request type must be an integer.")
        return True

    def validate_content(self) -> bool:
        if not isinstance(self._content, str) or not self._content.strip():
            raise ValueError("Ticket content cannot be empty.")
        return True

    def validate_urgency(self) -> bool:
        if not isinstance(self._urgency, int) or isinstance(self._urgency, bool):
            raise ValueError("Urgency must be an integer.")
        return True

    def validate_impact(self) -> bool:
        if not isinstance(self._impact, int) or isinstance(self._impact, bool):
            raise ValueError("Impact must be an integer.")
        return True

    def validate_priority(self) -> bool:
        if not isinstance(self._priority, int) or isinstance(self._priority, bool):
            raise ValueError("Priority must be an integer.")
        return True

    def validate_categories_id(self) -> bool:
        if not isinstance(self._categories_id, int) or isinstance(self._categories_id, bool):
            raise ValueError("Category id must be an integer.")
        return True

    def validate_type(self) -> bool:
        if not isinstance(self._type, int) or isinstance(self._type, bool):
            raise ValueError("Ticket type must be an integer.")
        return True

    def validate_slas_id_ttr(self) -> bool:
        if not isinstance(self._slas_id_ttr, int) or isinstance(self._slas_id_ttr, bool):
            raise ValueError("TTR SLA id must be an integer.")
        return True

    def validate_slas_id_tto(self) -> bool:
        if not isinstance(self._slas_id_tto, int) or isinstance(self._slas_id_tto, bool):
            raise ValueError("TTO SLA id must be an integer.")
        return True

    def validate_time_to_resolve(self) -> bool:
        if not isinstance(self._time_to_resolve, datetime.datetime):
            raise ValueError("Time to resolve must be a datetime.")
        return True

    def validate_time_to_own(self) -> bool:
        if not isinstance(self._time_to_own, datetime.datetime):
            raise ValueError("Time to own must be a datetime.")
        return True

    def validate_name_user(self) -> bool:
        if not isinstance(self._name_user, str) or not self._name_user.strip():
            raise ValueError("User name cannot be empty.")
        return True

    def validate(self) -> bool:
        return (
            self.validate_id()
            and self.validate_entities_id()
            and self.validate_title_ticket()
            and self.validate_date_ticket()
            and self.validate_request_types()
            and self.validate_content()
            and self.validate_urgency()
            and self.validate_impact()
            and self.validate_priority()
            and self.validate_categories_id()
            and self.validate_type()
            and self.validate_slas_id_ttr()
            and self.validate_slas_id_tto()
            and self.validate_time_to_resolve()
            and self.validate_time_to_own()
            and self.validate_name_user()
        )
