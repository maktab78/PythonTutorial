# class Fly:
#     bag = []
#     height = 120
#
#     def flying(self):
#         print("IN Sky !!!")
#
#
# class BaseUser:
#     def __init__(self, name, family) -> None:
#         self.name = name
#         self.family = family
#
#
# class EnUser(BaseUser):
#     def say_hello(self):
#         print("Hello", self.name, self.family)
#
#
# class FaUser(BaseUser, Fly):
#     def say_hello(self):
#         print("سلام ", self.name, self.family)


# david = EnUser('david', 'Alipoor')
# david.say_hello()

# ali = FaUser('علی', 'رضایی')
# ali.say_hello()
# ali.flying()

# from requests import get
#
#
# class HeaderMixin:
#     def get_header(self):
#         print('header is ................')
#
#
# class Request(HeaderMixin):
#     def __init__(self, url):
#         self.url = url
#
#     def get(self):
#         print(get(self.url).text)
#
#
# get_ip = Request('https://icanhazip.com')
# get_ip.get_header()
# get_ip.get()

from abc import ABC, abstractmethod
from time import sleep


# Pattern - Template - Base
class BaseWeapon(ABC):

    @abstractmethod
    def fire(self):
        raise NotImplementedError

    @abstractmethod
    def reload(self):
        raise NotImplementedError


# Use Base - Initialize
class Weapon(BaseWeapon):

    def __init__(self, damage: int, reload_time: int, bag: int):
        self.damage = damage
        self.bag = bag
        self.reload_time = reload_time

    def fire(self):
        self.bag -= 1 if self.bag != 0 else self.bag
        print('fire !!!' if self.bag else 'Please reload.')

    def reload(self):
        sleep(self.reload_time)
        print('Reload successful')


class Gun(Weapon):  # inheritance
    pass


class Blade(Weapon):  # inheritance
    def fire(self):  # polymorphism
        pass


# Sniper -> Awp, M24
# Pistol -> P11, Dissert
# Extension -> Laser, Scope, Silencer
# Assault Rifle -> M416 - Ak47
# Extension -> Laser, Scope, Silencer
# Blade -> Knife
# Extension -> KnifeColor
# Item -> Smoke, Flash, Grenade, Shield, Helmet
#
