from typing import List


class Pizza:
    """
    Base class for pizzas
    """

    def __init__(self, name: str, ingredients: List[str]):
        """
        Initialize a pizza

        :param name: The name of the pizza
        :param ingredients: List of ingredients
        """
        self.name = name
        self.ingredients = ingredients

    def dict(self) -> dict:
        """
        Return a recipe for the pizza
        """
        result = {"name": self.name, "ingredients": self.ingredients}
        return result

    def __eq__(self, other) -> bool:
        """Checking whether two pizzas from one type"""
        if isinstance(other, Pizza):
            return self.ingredients == other.ingredients
        raise TypeError("You need to compare TWO PIZZA")


class Margherita(Pizza):
    """
    Margherita pizza
    """

    def __init__(self, size: str = "XL"):
        """
        Initialize a Margherita pizza

        :param size: The size of the pizza (L or XL).
        Default value XL
        """
        name = "Margherita"
        ingredients = ["tomato sauce", "mozzarella", "tomatoes"]
        super().__init__(name, ingredients)
        self.size = size


class Pepperoni(Pizza):
    """
    Pepperoni pizza
    """

    def __init__(self, size: str = "XL"):
        """
        Initialize a Pepperoni pizza

        :param size: The size of the pizza (L or XL).
        Default value XL
        """
        name = "Pepperoni"
        ingredients = ["tomato sauce", "mozzarella", "pepperoni"]
        super().__init__(name, ingredients)
        self.size = size


class Hawaiian(Pizza):
    """
    Hawaiian pizza
    """

    def __init__(self, size: str = "XL"):
        """
        Initialize a Hawaiian pizza.

        :param size: The size of the pizza (L or XL).
        Default value XL
        """
        name = "Hawaiian"
        ingredients = ["tomato sauce", "mozzarella", "chicken", "pineapples"]
        super().__init__(name, ingredients)
        self.size = size
