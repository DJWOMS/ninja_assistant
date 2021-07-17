from ninja import Schema


class GoogleAuth(Schema):
    token: str
    picture: str
    email: str


class Token(Schema):
    id: int
    token: str
