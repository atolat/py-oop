"""
Abstract Factory Method for Pizza Store
"""

from abc import ABC, abstractmethod

"""
Pizza - Product Class
Factories produce products, and in the PizzaStore, our product is a Pizza.
"""


class Pizza(ABC):

    @abstractmethod
    def __init__(self):
        self._name = None
        self._dough = None
        self._sauce = None
        self._toppings = []

    def prepare(self):
        print("Preparing " + self._name)
        print("Tossing dough...")
        print("Adding sauce...")
        print("Adding toppings: ")
        print("   ".join(self._toppings))

    def bake(self):
        print("Bake for 25 minutes at 350")

    def cut(self):
        print("Cutting the pizza into diagonal slices")

    def box(self):
        print("Place pizza in official PizzaStore box")

    def get_name(self):
        return self._name

    def __str__(self):
        display = ""
        display += "---- " + self._name + " ----\n"
        display += self._dough + "\n"
        display += self._sauce + "\n"
        display += "\n".join(self._toppings)
        return display


"""
Pizza Store - Creator Class
This is our abstract creator class. 
It defines an abstract factory method that the subclasses implement to produce products.
"""


class PizzaStore(ABC):

    # create_pizza is now an abstract factory method in PizzaStore
    @abstractmethod
    def create_pizza(self, item: str) -> Pizza:
        pass

    def order_pizza(self, pizza_type: str) -> Pizza:
        pizza = self.create_pizza(pizza_type)
        print("--- Making a " + pizza.get_name() + " ---")

        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

        return pizza


# Concrete implementations of the Creator Class
class NYPizzaStore(PizzaStore):

    def create_pizza(self, item: str) -> Pizza:
        if item == "cheese":
            return NYStyleCheesePizza()
        elif item == "veggie":
            return NYStyleVeggiePizza()
        elif item == "clam":
            return NYStyleClamPizza()
        elif item == "pepperoni":
            return NYStylePepperoniPizza()
        else:
            return None


class ChicagoPizzaStore(PizzaStore):

    def create_pizza(self, item: str) -> Pizza:
        if item == "cheese":
            return ChicagoStyleCheesePizza()
        elif item == "veggie":
            return ChicagoStyleVeggiePizza()
        elif item == "clam":
            return ChicagoStyleClamPizza()
        elif item == "pepperoni":
            return ChicagoStylePepperoniPizza()
        else:
            return None


# Concrete product implementations
class NYStyleCheesePizza(Pizza):

    def __init__(self):
        super(NYStyleCheesePizza, self).__init__()
        self._name = "NY Style Sauce and Cheese Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")


class NYStylePepperoniPizza(Pizza):

    def __init__(self):
        super(NYStylePepperoniPizza, self).__init__()
        self._name = "NY Style Pepperoni Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Sliced Pepperoni")
        self._toppings.append("Garlic")
        self._toppings.append("Onion")
        self._toppings.append("Mushrooms")
        self._toppings.append("Red Pepper")


class NYStyleClamPizza(Pizza):

    def __init__(self):
        super(NYStyleClamPizza, self).__init__()
        self._name = "NY Style Clam Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"
        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Fresh Clams from Long Island Sound")


class NYStyleVeggiePizza(Pizza):

    def __init__(self):
        super(NYStyleVeggiePizza, self).__init__()
        self._name = "NY Style Veggie Pizza"
        self._dough = "Thin Crust Dough"
        self._sauce = "Marinara Sauce"

        self._toppings.append("Grated Reggiano Cheese")
        self._toppings.append("Garlic")
        self._toppings.append("Onion")
        self._toppings.append("Mushrooms")
        self._toppings.append("Red Pepper")


class ChicagoStyleCheesePizza(Pizza):

    def __init__(self):
        super(ChicagoStyleCheesePizza, self).__init__()
        self._name = "Chicago Style Deep Dish Cheese Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"
        self._toppings.append("Shredded Mozzarella Cheese")

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStylePepperoniPizza(Pizza):

    def __init__(self):
        super(ChicagoStylePepperoniPizza, self).__init__()
        self._name = "Chicago Style Pepperoni Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Black Olives")
        self._toppings.append("Spinach")
        self._toppings.append("Eggplant")
        self._toppings.append("Sliced Pepperoni")

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStyleClamPizza(Pizza):

    def __init__(self):
        super(ChicagoStyleClamPizza, self).__init__()
        self._name = "Chicago Style Clam Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Frozen Clams from Chesapeake Bay")

    def cut(self):
        print("Cutting the pizza into square slices")


class ChicagoStyleVeggiePizza(Pizza):

    def __init__(self):
        super(ChicagoStyleVeggiePizza, self).__init__()
        self._name = "Chicago Deep Dish Veggie Pizza"
        self._dough = "Extra Thick Crust Dough"
        self._sauce = "Plum Tomato Sauce"

        self._toppings.append("Shredded Mozzarella Cheese")
        self._toppings.append("Black Olives")
        self._toppings.append("Spinach")
        self._toppings.append("Eggplant")

    def cut(self):
        print("Cutting the pizza into square slices")


# Driver Code
if __name__ == '__main__':
    nyStore = NYPizzaStore()
    chicagoStore = ChicagoPizzaStore()

    pizza = nyStore.order_pizza("cheese")
    print("Ethan ordered a " + pizza.get_name() + "\n")

    pizza = chicagoStore.order_pizza("cheese")
    print("Joel ordered a " + pizza.get_name() + "\n")

    pizza = nyStore.order_pizza("clam")
    print("Ethan ordered a " + pizza.get_name() + "\n")

    pizza = chicagoStore.order_pizza("clam")
    print("Joel ordered a " + pizza.get_name() + "\n")

    pizza = nyStore.order_pizza("pepperoni")
    print("Joel ordered a " + pizza.get_name() + "\n")

    pizza = chicagoStore.order_pizza("pepperoni")
    print("Ethan ordered a " + pizza.get_name() + "\n")

    pizza = nyStore.order_pizza("veggie")
    print("Joel ordered a " + pizza.get_name() + "\n")
