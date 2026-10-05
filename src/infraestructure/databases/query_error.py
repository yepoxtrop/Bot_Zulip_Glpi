class QueryError(Exception):

    def __init__(self, id:int,  msg:str, code:int):
        super().__init__(msg);
        self.code = code;