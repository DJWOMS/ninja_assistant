from ninja import Schema


class UserOut(Schema):
    id: int
    # first_name: str
    # last_name: str
    username: str
    avatar: str
