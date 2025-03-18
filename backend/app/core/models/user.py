from tortoise import fields

from core.models import Base


class User(Base):
    telegram_id = fields.BigIntField(unique=True, db_index=True)
    first_name = fields.CharField(max_length=255)
    last_name = fields.CharField(max_length=255, null=True)
    username = fields.CharField(max_length=255, null=True)
    birth_date = fields.DateField(null=True)

    def __str__(self):
        return self.username
