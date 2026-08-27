class QueryError(Exception):

    def __init__(self, msg:str, code:int):
        super().__init__(msg);
        self.code = code;
