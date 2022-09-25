# Association between classes occurs when a class has 
# attributes that are objects of another class. In line 
# with this concept, look at the class diagram below, which 
# represents an association where a Person owns a Car.

# ---------------                   --------------
# | Person      |                   | Car        |
# ---------------       has         --------------
# | name: str   |------------------ | brand: str |
# | age: int    |1                 1| model: str |
# | car: Car    |                   | plate: str |
# ---------------                   | year: int  |
#                                   -------------- 

# Implement the Person and Car classes.


class Car:
    def __init__(self, brand, model, plate, year):
        self.brand = brand
        self.model = model
        self.plate = plate
        self.year = year


class Person:
    def __init__(self, name, age, car):
        self.name = name
        self.age = age
        self.car = car


mycar = Car('Volkswagen', 'Gol', 'AAA-1111', 2015)
me = Person('João', 25, mycar)
print('Name: ', me.name)
print('Age: ', me.age)
print('Brand of the car: ', me.car.brand)
print('Model of the car: ', me.car.model)
print('Plate of the car: ', me.car.plate)
print('Year of the car: ', me.car.year)
