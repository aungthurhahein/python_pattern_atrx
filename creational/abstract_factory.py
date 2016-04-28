# -*- coding: utf-8 -*-
# @Author: aung
# @Date:   2016-04-28 15:02:12
# @Last Modified by:   aung
# @Last Modified time: 2016-04-28 15:55:40

# http://ginstrom.com/scribbles/2007/10/08/design-patterns-python-style/

# abstract factory pattern: a generic function for specific classes
import random


# factory
class CarShop:

    def __init__(self,vehicle_factory=None):
        self.car_factory = vehicle_factory
     
    def show_car(self):
        car = self.car_factory.get_car()
        print("We have a lovely {}".format(car))
        print ("It can {}".format(car.wheels()))
        print("It is {}".format(car.speak()))
        print("It uses {}".format(self.car_factory.car_gas()))


# factory items
class Van:
    def speak(self):
        return "big"
    def wheels(self):
        return("carry goods")
    def __str__(self):
        return "Van"

class Sedan:
    def speak(self):
        return "comfy"
    def wheels(self):
        return("carry 4 people")
    def __str__(self):
        return "Sedan"


# factor classes
class VanFactory:
    def get_car(self):
        return Van()
    def 
    def car_gas(self):
        return "Disel"

class SedanFactory:
    def get_car(self):
        return Sedan()

    def car_gas(self):
        return "electric"

# Create the factory wrapper
def get_factory():
    """Let's be dynamic!"""
    return random.choice([VanFactory, SedanFactory])()

if __name__ == "__main__":
    for i in range(3):
        shop = CarShop(get_factory())
        shop.show_car()
        print("=" * 20)
