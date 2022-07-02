from peewee import *
import datetime

db = MySQLDatabase("test", host="127.0.0.1", port=3306, user="root", passwd="root")
db.connect()

class BaseModel(Model):

    class Meta:
        database = db

class User(BaseModel):
    username = CharField(unique=True)

class Tweet(BaseModel):
    user = ForeignKeyField(User, related_name='tweets')
    message = TextField()
    created_date = DateTimeField(default=datetime.datetime.now)
    is_published = BooleanField(default=True)

if __name__ == "__main__":
    user = User.create(username='tom')

