from ninja import Schema


class GoogleAuth(Schema):
    token: str
    picture: str
    email: str


class Token(Schema):
    id: int
    access_token: str
    token_type: str


class TokenAuth(Schema):
    id: int
    exp: str
    sub: str
