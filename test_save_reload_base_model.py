#!/usr/bin/python3
from models.storage import all
from models.base_model import BaseModel

all_objs = all()
print("-- Reloaded objects --")
for key, obj in all_objs.items():
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
try:
    my_model.save()
    print(my_model)
except Exception as e:
    print("An error occurred while saving the model:", str(e))
