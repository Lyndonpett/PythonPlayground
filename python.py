#!/usr/bin/python3
""" talk about imports and how to work with them"""

# if __name__ == "__main__": # what is this doing?
#     from variable_load_2 import a # here we are importing a variable from another file
#     import variable_load_2 # here we are importing the entire file

#     print(variable_load_2.a)
#     print(a)

""" be sure you know about built in modules and how to use them:
    max, min, sum, sorted, map, etc."""

# def best_score(a_dictionary):
#     if a_dictionary:
#         return(max(a_dictionary, key=a_dictionary.get))

# class Square:
#     """This define class and instantiates a private attribute"""

#     def __init__(self, size=0):
#         self.__size = size

#     @property # a decorator, which acts as a wrapper function, in this case it defaults back to the getter
#     def size(self):
#         return self.__size

#     @size.setter # this is the setter, again using a decorator
#     def size(self, value):
#         if type(value) is not int:
#             raise TypeError("size must be an integer")

#         elif value < 0:
#             raise ValueError("size must be >= 0")

#         else:
#             self.__size = value

#     def area(self):
#         squareArea = self.__size * self.__size
#         return squareArea
"""Remember we can set override __repr__ methods to return what we want, same with print and __str__"""

""" Lets talk about unittests"""

# def max_integer(list=[]):
#     """Function to find and return the max integer in a list of integers
#         If the list is empty, the function returns None
#     """
#     if len(list) == 0:
#         return None
#     result = list[0]
#     i = 1
#     while i < len(list):
#         if list[i] > result:
#             result = list[i]
#         i += 1
#     return result



# """Lets talk about classes and inheritance"""
# class BaseGeometry:
#     "Raises exception for area"

#     def area(self):
#         raise Exception("area() is not implemented")

#     """Validates value"""

#     def integer_validator(self, name, value):
#         if type(value) is not int:
#             raise TypeError("{} must be an integer".format(name))
#         if value <= 0:
#             raise ValueError("{} must be greater than 0".format(name))

# class Rectangle(BaseGeometry):
#     """Defines the Rectangle class"""

#     def __init__(self, width, height):
#         self.integer_validator("width", width)
#         self.__width = width
#         self.integer_validator("height", height)
#         self.__height = height

#     def area(self):
#         return self.__height * self.__width

#     def __str__(self):
#         return "[Rectangle] {}/{}".format(self.__width, self.__height)


""" airbnb console tips """

import json

# JSON string
students = '{"id":"9607", "name": "Sunny", "department":"Computer"}'

# convert string to Python dict --- json.loads() method can be used to parse a valid JSON string and convert it into a Python Dictionary
student_dict = json.loads(students)
print(student_dict)

print('Deserialized ' + student_dict['name'])


data = {
  "id": "877",
  "name": "Mayur",
  "department": "Comp"
}

# Serializing json --- json.dumps() method can be used to convert a Python Dictionary into a JSON string
json_object = json.dumps(data)
print('Serialized ' + json_object)

"""you will create all of the serializers and deserializers for your models in a engine/filestorage file"""
"""In this you will have to create a class that will handle the serialization and deserialization of your models"""
"""Will also have to handle reloading and deleting of objects"""

import cmd
import readline

""" this is running and setting up a console for you to use"""
""" you can add new commands to this console by adding them to the class, as well as give their help text in the doc string"""
class HBNBCommand(cmd.Cmd):
    '''Console class for builtin commands'''

    prompt = '(hbnb) '

    def do_quit(self, args):
        '''Exits the application'''
        raise SystemExit

    def do_EOF(self, args):
        '''Exits application on End of File'''
        raise SystemExit

    def emptyline(self):
        '''oryihgu'''
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()


"""this is the base model class
 everything will inherit from this class, and it will handle the creation of the id and the updated_at and created_at attributes"""
import uuid
from datetime import datetime
import models


class BaseModel:
    '''Base model for future classes'''

    def __init__(self, **kwargs):
        '''init method of BaseModel'''
        if kwargs:
            for key in kwargs:
                if key in ('created_at', 'updated_at'):
                    kwargs[key] = datetime.strptime(
                        kwargs[key], '%Y-%m-%dT%H:%M:%S.%f')
                if key != ('__class__'):
                    setattr(self, key, kwargs[key])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        models.storage.new(self)

    def __str__(self):
        '''string representation of the BaseModel'''
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        '''Updates update_at attribute with current date/time'''
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self):
        '''return dictionary containing key:value from __dict__'''
        newDic = self.__dict__.copy()
        newDic['__class__'] = self.__class__.__name__
        newDic['created_at'] = self.created_at.isoformat()
        newDic['updated_at'] = self.updated_at.isoformat()

        return newDic

"""eventually youll be able to create files in a json file, but next youll use mysql"""

# https://github.com/Lyndonpett/AirBnB_clone/blob/main/README.md
