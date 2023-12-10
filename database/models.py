from peewee import *
from data.config import *

db = PostgresqlDatabase(database=DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)


class BaseModel(Model):

    class Meta:
        database = db


class User(BaseModel):
    telegram_id = BigIntegerField(primary_key=True)
    full_name = CharField(max_length=255)
    username = CharField(max_length=255, null=True)
    join_date = DateTimeField(formats=["%Y-%m-%d %H:%M:%S"])

    class Meta:
        db_name = "users"


