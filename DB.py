from peewee import *

db = SqliteDatabase('data.db')


class BaseModel(Model):
    class Meta:
        database = db


class Content(BaseModel):
    class Meta:
        db_table = 'Contents'

    first_name = CharField()
    last_name = CharField()
    middle_name = CharField(null=True)
    phone = TextField()
    email = TextField()
    vk = TextField()
    content = TextField()

    @classmethod
    def table_create(cls):
        cls.create_table()
