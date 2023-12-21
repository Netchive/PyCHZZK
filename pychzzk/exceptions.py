class PyChzzkException(Exception):
    def __init__(self, message: str):
        self.message = message


class PyChzzkHTTPException(PyChzzkException):
    def __init__(self, message: str, code: int):
        super().__init__(message)
        self.code = code

__all__ = [
    PyChzzkException,
    PyChzzkHTTPException
]