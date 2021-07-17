from ninja.orm import create_schema
from .models import User

UserOut = create_schema(User, fields=['id', 'username', 'avatar'])

