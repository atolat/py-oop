"""
Starbuzz coffee

Design for a coffee shop vending machine that has 4 main offerings
- House Blend
- Dark Roast
- Espresso
- Decaf

Each of these can be combined witha variety of condiments like steamed milk, soy miolk, mocha, whip, etc. that come at an extra charge
The order system must return the cost of a given order with condiments.
"""

from abc import ABC, abstractmethod


# Beverages
'''
The beverage class acts as an Abstract Component Class
Each beverage is a concrete implementation of this class
'''
class Beverage(ABC):
    def __init__(self):
        self._description = "Unknown Beverage"

    def get_description(self):
        return self._description

    @abstractmethod
    def cost(self):
        pass


class HouseBlend(Beverage):

    def __init__(self):
        self._description = "House Blend Coffee"

    def cost(self):
        return .89


class DarkRoast(Beverage):

    def __init__(self):
        self._description = "Dark Roast Coffee"

    def cost(self):
        return .99


class Espresso(Beverage):

    def __init__(self):
        self._description = "Espresso"

    def cost(self):
        return 1.99


class Decaf(Beverage):

    def __init__(self):
        self._description = "Decaf Coffee"

    def cost(self):
        return 1.05


# Condiment decorators
'''
Decorators implement the same interface as the concrete class they are going to decorate.
They extend the state of a component.
In our example, each decorator adds the condiment's name to the description and price to the cost.
'''

class CondimentDecorator(Beverage):
    @abstractmethod
    def get_description(self):
        pass


class Milk(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Milk"

    def cost(self):
        return .10 + self._beverage.cost()


class Mocha(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Mocha"

    def cost(self):
        return .20 + self._beverage.cost()


class Soy(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Soy"

    def cost(self):
        return .15 + self._beverage.cost()


class Whip(CondimentDecorator):

    def __init__(self, beverage):
        self._beverage = beverage

    def get_description(self):
        return self._beverage.get_description() + ", Whip"

    def cost(self):
        return .10 + self._beverage.cost()


###############################################################################
# Simulation
###############################################################################

if __name__ == '__main__':
    beverage = Espresso()
    print(beverage.get_description() + " $" + str(beverage.cost()))

    beverage2 = DarkRoast()
    beverage2 = Mocha(beverage2)
    beverage2 = Mocha(beverage2)
    beverage2 = Whip(beverage2)
    print(beverage2.get_description() + " $" + str(beverage2.cost()))

    beverage3 = HouseBlend()
    beverage3 = Soy(beverage3)
    beverage3 = Mocha(beverage3)
    beverage3 = Whip(beverage3)
    print(beverage3.get_description() + " $" + str(beverage3.cost()))