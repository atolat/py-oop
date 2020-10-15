"""
Final Abstract Factory Pattern
"""
from abc import ABC, abstractmethod

# Ingredients

# Cheese
class Cheese(ABC):

    @abstractmethod
    def __str__(self):
        pass


class MozzarellaCheese(Cheese):
    def __str__(self):
        return "Shredded Mozzarella"


class ParmesanCheese(Cheese):
    def __str__(self):
        return "Shredded Parmesan"


class ReggianoCheese(Cheese):
    def __str__(self):
        return "Reggiano Cheese"


# Clams
class Clams(ABC):
    @abstractmethod
    def __str__(self):
        pass


class FreshClams(Clams):
    def __str__(self):
        return "Fresh Clams from Long Island Sound"


class FrozenClams(Clams):
    def __str__(self):
        return "Frozen Clams from Chesapeake Bay"


# Dough
class Dough(ABC):

    @abstractmethod
    def __str__(self):
        pass


class ThickCrustDough(Dough):
    def __str__(self):
        return "Thin Crust Dough"


class ThinCrustDough(Dough):
    def __str__(self):
        return "ThickCrust style extra thick crust dough"


# Pepperoni
class Pepperoni(ABC):

    @abstractmethod
    def __str__(self):
        pass


class SlicedPepperoni(Pepperoni):
    def __str__(self):
        return "Sliced Pepperoni"


# Sauce
class Sauce(ABC):
    @abstractmethod
    def __str__(self):
        pass


class MarinaraSauce(Sauce):
    def __str__(self):
        return "Marinara Sauce"


class PlumTomatoSauce(Sauce):
    def __str__(self):
        return "Tomato sauce with plum tomatoes"


# Veggie
class Veggie(ABC):

    @abstractmethod
    def __str__(self):
        pass


class BlackOlives(Veggie):
    def __str__(self):
        return "Black Olives"


class Eggplant(Veggie):
    def __str__(self):
        return "Eggplant"


class Garlic(Veggie):
    def __str__(self):
        return "Garlic"


class Mushroom(Veggie):
    def __str__(self):
        return "Mushrooms"


class Onion(Veggie):
    def __str__(self):
        return "Onion"


class RedPepper(Veggie):
    def __str__(self):
        return "Red Pepper"


class Spinach(Veggie):
    def __str__(self):
        return "Spinach"


# Factories

class PizzaIngredientFactory(ABC):

    @abstractmethod
    def create_dough(self) -> Dough:
        pass

    @abstractmethod
    def create_sauce(self) -> Sauce:
        pass

    @abstractmethod
    def create_cheese(self) -> Cheese:
        pass

    @abstractmethod
    def create_veggies(self) -> Veggie:
        pass

    @abstractmethod
    def create_pepperoni(self) -> Pepperoni:
        pass

    @abstractmethod
    def create_clam(self) -> Clams:
        pass


class NYPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThinCrustDough()

    def create_sauce(self):
        return MarinaraSauce()

    def create_cheese(self):
        return ReggianoCheese()

    def create_veggies(self):
        return [Garlic(), Onion(),
                Mushroom(), RedPepper()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FreshClams()


class ChicagoPizzaIngredientFactory(PizzaIngredientFactory):

    def create_dough(self):
        return ThickCrustDough()

    def create_sauce(self):
        return PlumTomatoSauce()

    def create_cheese(self):
        return MozzarellaCheese()

    def create_veggies(self):
        return [BlackOlives(), Spinach(),
                Eggplant()]

    def create_pepperoni(self):
        return SlicedPepperoni()

    def create_clam(self):
        return FrozenClams()


# Pizzas

class Pizza(ABC):
    def __init__(self):
        self._name = None
        self._dough = None
        self._sauce = None
        self._veggies = []
        self._cheese = None
        self._pepperoni = None
        self._clam = None

    @abstractmethod
    def prepare(self):
        pass

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def set_name(self, name):
        self._name = name

    def get_name(self):
        return self._name

    def __str__(self):
        result = "---- " + self._name + " ----\n"

        if self._dough is not None:
            result += str(self._dough) + "\n"

        elif self._sauce is not None:
            result += str(self._sauce) + "\n"

        elif self._cheese is not None:
            result += str(self._cheese) + "\n"

        elif self._veggies is not None:
            result += ", ".join(self._veggies) + "\n"

        elif self._clam is not None:
            result += str(self._clam) + "\n"

        elif self._pepperoni is not None:
            result += str(self._pepperoni) + "\n"

        return result


class CheesePizza(Pizza):

    def __init__(self, ingredient_factory):
        super(CheesePizza, self).__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self._name)
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()


class ClamPizza(Pizza):

    def __init__(self, ingredient_factory):
        super(ClamPizza, self).__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self._name)

        self._cheese = self._ingredient_factory.create_cheese()
        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._clam = self._ingredient_factory.create_clam()


class PepperoniPizza(Pizza):

    def __init__(self, ingredient_factory):
        super(PepperoniPizza, self).__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self._name)

        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()
        self._pepperoni = self._ingredient_factory.create_pepperoni()


class VeggiePizza(Pizza):

    def __init__(self, ingredient_factory):
        super(VeggiePizza, self).__init__()
        self._ingredient_factory = ingredient_factory

    def prepare(self):
        print("Preparing " + self._name)

        self._dough = self._ingredient_factory.create_dough()
        self._sauce = self._ingredient_factory.create_sauce()
        self._cheese = self._ingredient_factory.create_cheese()
        self._veggies = self._ingredient_factory.create_veggies()


# Stores

class PizzaStore(ABC):

    @abstractmethod
    def create_pizza(self, item: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type):
        pizza = self.create_pizza(pizza_type)
        print("--- Making a " + pizza.get_name() + " ---")

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


class NYPizzaStore(PizzaStore):

    def create_pizza(self, item):
        pizza = None
        ingredient_factory = NYPizzaIngredientFactory()

        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("New York Style Cheese Pizza")

        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("New York Style Veggie Pizza")

        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("New York Style Clam Pizza")

        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("New York Style Pepperoni Pizza")

        return pizza


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, item):
        pizza = None
        ingredient_factory = ChicagoPizzaIngredientFactory()

        if item == "cheese":
            pizza = CheesePizza(ingredient_factory)
            pizza.set_name("Chicago Style Cheese Pizza")

        elif item == "veggie":
            pizza = VeggiePizza(ingredient_factory)
            pizza.set_name("Chicago Style Veggie Pizza")

        elif item == "clam":
            pizza = ClamPizza(ingredient_factory)
            pizza.set_name("Chicago Style Clam Pizza")

        elif item == "pepperoni":
            pizza = PepperoniPizza(ingredient_factory)
            pizza.set_name("Chicago Style Pepperoni Pizza")

        return pizza

# Driver Code


if __name__ == '__main__':
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza("cheese")
    print("Ethan ordered a " + str(pizza) + "\n")

    pizza = chicagoStore.order_pizza("cheese")
    print("Joel ordered a " + str(pizza) + "\n")

    pizza = nyStore.order_pizza("clam")
    print("Ethan ordered a " + str(pizza) + "\n")

    pizza = chicagoStore.order_pizza("clam")
    print("Joel ordered a " + str(pizza) + "\n")

    pizza = nyStore.order_pizza("pepperoni")
    print("Ethan ordered a " + str(pizza) + "\n")

    pizza = chicagoStore.order_pizza("pepperoni")
    print("Joel ordered a " + str(pizza) + "\n")

    pizza = nyStore.order_pizza("veggie")
    print("Ethan ordered a " + str(pizza) + "\n")

    pizza = chicagoStore.order_pizza("veggie")
    print("Joel ordered a " + str(pizza) + "\n")
