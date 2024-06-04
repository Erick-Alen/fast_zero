from fastapi import HTTPException, status


class CredentialsException(HTTPException):
    def __init__(
        self,
        detail: str = 'Could not validate credentials',
        headers: dict = None,
        extra_info: dict = None,
    ):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers=headers,
        )
