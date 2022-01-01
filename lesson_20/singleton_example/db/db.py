from lesson_21.singleton_example.singleton import singleton


@singleton
class DbConnection:
    """Represent connection to database"""
    def __init__(
        self,
        host: str,
        port: int,
    ) -> None:
        self.__host = host
        self.__port = port

    @property
    def host(self):
        return self.__host
