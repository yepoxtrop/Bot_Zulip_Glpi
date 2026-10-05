import datetime;

class Chat:
    def __init__(self, id:int, serial:str, user, date_satart:datetime.datetime):
        self.__id = id; 
        self._serial = serial;
        self._status = True;
        self._date_start = date_satart;
        self._date_end = None;
        self._messages = None;
        self._process = None;
        self._users = [user];
        self._steps = None;