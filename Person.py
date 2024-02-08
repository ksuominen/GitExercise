class Person:
    def __init__(self, name: str, age: int):
        self.__name = name
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @property
    def age(self):
        return self.__age
    
    @name.setter
    def name(self, name):
        self.__name = name

    @age.setter
    def age(self, age):
        self.__age = age

    def __str__(self):
        return f"{self.__name}, {self.__age} years old"
