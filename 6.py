"""
- PascalCase => Reza Yazdani --> RezaYazdani --> classes
- camelCase => Reza Yazdani --> rezaYazdani --> ??? ()
- snake_case => Reza Yazdani --> reza_yazdani --> methods + functions
"""

from random import randrange
from uuid import uuid4


class Product:

    def __init__(self, **kwargs) -> None:
        for key in kwargs:
            setattr(self, key, kwargs[key])


class Shop:
    # Data :
    __COUNT = 0
    __OWNERS = []

    # Magic Attribute => reporter
    __owners__ = f"""
        count of registered shops : {__COUNT}
        owners : {__OWNERS}
    """

    """
        sample_name : public
        _sample_name : protect
        __sample_name : private
        __sample_name__ : magic attribute
    """

    # constants = [
    #     "name",  # +readable, -writable
    #     "code",  # +readable, -writable
    # ]

    class __Utils:

        @classmethod
        def code_generator(cls):
            return str(uuid4()).split('-')[0]

    class Validators:
        pass

    def __init__(self, owner: str, name: str) -> None:
        self.inventory = []
        self.owner = owner
        self._name = name
        self.__password = str(randrange(100, 1000, 100))
        self.__code = self.__Utils.code_generator()

        self.__class__.__COUNT += 1
        self.__class__.__OWNERS.append(owner)

        print(f"Your shop code is {self.__code}")

    def add_product(self, product: Product) -> None:
        if isinstance(product, Product):
            self.inventory.append(product)

    @property
    def password(self):
        return f"{self.__password[0]}**"

    def change_password(self, old_password, new_password):
        if self.login(old_password):
            self.__password = new_password

    def _forget_password(self, code):
        if code == self.__code:
            print(f"your password is : {self.__password}")

    def login(self, password):
        return password == self.__password


shop1 = Shop("reza", "reza Chicken")
shop2 = Shop("amir", "amir Chicken")
shop3 = Shop("nazgol", "nazgol Chicken")

# Public
print(shop1.owner)
shop1.owner = "Asghar"
print(shop1.owner)

# Protect (Fake Private)
print(shop1._name)

# Private:
print(shop1.password)


print(Shop.__owners__)


