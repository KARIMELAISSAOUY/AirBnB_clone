#!/usr/bin/python3
from models.storage import all
from models.base_model import BaseModel
from models.user import User

all_objs = all()
print("-- Reloaded objects --")
for obj in all_objs.values():
    print(obj)

print("-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
try:
    my_user.save()
    print(my_user)
except Exception as e:
    print("An error occurred while saving the user:", str(e))

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
try:
    my_user2.save()
    print(my_user2)
except Exception as e:
    print("An error occurred while saving the user:", str(e))
