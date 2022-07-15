# class Human:
#     __COUNTER: int = 0
#
#     # HUMANS = []
#
#     def __init__(self, name: str, age: int):
#         # self.__class__.HUMANS.append(self)
#         self.__class__.__COUNTER += 1
#         self.name = name
#         self.age = age
#
#     @classmethod
#     def get_counter(cls):
#         return cls.__COUNTER
#
#
# reza = Human('reza', 22)
# ali = Human('ali', 22)
# mohammad = Human('mohammad', 22)
# akbar = Human('akbar', 22)
#
# print(Human.get_counter())
#
#
# # print(Human.HUMANS)
# # print(Human.HUMANS[0])
#
#
# class Staff(Human):
#
#     def __init__(self, name: str, age: int, staff_id: int):
#         super().__init__(name, age)
#         self.staff_id = staff_id
#
#
# class Book:
#     pass
#
#
# class Category:
#     pass
#
#
# class Cage:
#     pass
#
#
# class Library:
#
#     # aggregation
#     def __init__(self, staff) -> None:
#         self.staff = staff
#
#     # composition
#     # def __init__(self, name, age, staff_id):
#     #     self.staff = Staff(name, age, staff_id)
#
#
# mr_alizade = Staff('alizade', 34, 2323452342)
# print(mr_alizade.staff_id)
#
#
# central_lib = Library(mr_alizade)
#
# print(central_lib.staff.name)
# del central_lib
#
# private_lib = Library(mr_alizade)

class Log:
    def __init__(self, mode, status, comment):
        self.mode = mode
        self.status = status
        self.comment = comment


class LoggerMixin:
    def __init__(self):
        self.logs = {}

    def add_log(self, mode, status, comment):
        self.logs[mode] = Log(mode, status, comment)


class Wallet(LoggerMixin):
    __COUNTER = 0
    __BACKUPS = {}

    def __init__(self, name) -> None:

        self.name = name
        super(Wallet, self).__init__()
        self.__class__.__COUNTER += 1
        self.__code = self.__class__.__COUNTER
        print("Your private code is:", self.__code)
        self.__class__.__BACKUPS[self.__code] = self
        self.storage = {}

    def __repr__(self):
        return self.name + " Wallet"

    def add_money(self, money):
        if isinstance(money, Money):
            self.storage['money'][money.type] += money.value

    @classmethod
    def restore(cls, code):
        if code in cls.__BACKUPS:
            return cls.__BACKUPS[code]


class Money:
    M_TYPE = ('T', 'R', 'D', 'E')

    def __init__(self, m_type: str, value: int) -> None:
        self.type = m_type.upper() if m_type.upper() in self.__class__.M_TYPE else None
        self.value = value

        if not self.type:
            print('Please enter valid money type! [ T, R, D, E ]')
            # error!


class Card:
    pass


class Receipt:
    pass


my_wallet = Wallet('reza')