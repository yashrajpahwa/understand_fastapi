from fastapi import HTTPException


class DemoException(HTTPException):
    def __init__(self, message: str = "Demo exception") -> None:
        super().__init__(status_code=418, detail=message)
