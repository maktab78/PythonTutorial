from typing import Any


class Bank:
    # class attr
    list_of_banks = []

    # self -> instance
    # cls = self.__class__ = Bank -> class object

    # METHOD INITIALIZER
    def __init__(self, name: str) -> None:
        self.name = name
        self.code = 7878

        # add to bank list
        # Bank.list_of_banks.append(self)
        self.__class__.list_of_banks.append(self)


sepah_bank = Bank('Sepah iranian')
melat_bank = Bank('Melat iranian')

# attr :
# print(f"{sepah_bank.name = }", f"{sepah_bank.code = }")
# Instance
sepah_bank.code = 4545

melli_bank = Bank('Melli iranian')


# print(melli_bank.code) # 7878

# [print(obj.name, obj.code) for obj in Bank.list_of_banks]


class Checker:

    @staticmethod
    def check_valid_balance(minimum_balance, new_balance):
        return True if minimum_balance < new_balance else False


class Account:

    def __init__(self, username: str, balance: float, **kwargs) -> None:
        # Private -> __xxxxx
        self.__fee = 500
        self.__minimum_balance = 5000

        # Validator
        self.__balance = balance if Checker.check_valid_balance(self.__minimum_balance, balance) else 0
        self.username = username

        for key in kwargs:
            setattr(self, key, kwargs[key])

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, new_balance):
        self.__balance = new_balance \
            if Checker.check_valid_balance(self.__minimum_balance, new_balance) else self.__balance

    def data(self):
        print(*[attr for attr in self.__dict__.items() if '_Account' not in attr[0]])


ali = Account('Ali Akbari', 30000, father_name='Heydar', age=33)
# print("Ali Balance:", ali.balance)
ali.balance -= 24000
# print("Ali Balance:", ali.balance)
ali.balance -= 6000
# print("Ali Balance:", ali.balance)

# print('\n\n\n\n')
# ali.father_name = "Mahmood"


ali.data()


# # Getter !
# def balance(self) -> float:
#     return self.your_balance
#
# #  Setter !
# def edit_balance(self, new_balance) -> None:
#     if self.balance() < self.minimum_balance:
#         # Error !
#         print('------ Failed! ------')
#         return None
#
#     self.your_balance = new_balance


# ali = Account('Alireza', 30000)
#
# print('$ :', ali.balance())
# ali.edit_balance(300)

# args , kwargs:*har,

# def variables(age, *har, **kw):
#     print(type(har))
#     for index, value in enumerate(har):
#         print(index, ":", value)
#
#     print(type(kw))
#     for key, value in kw.items():
#         print(key, ":", value)
#
#
# variables(10, 'reza', 343434, None, True, name='Alireza', family="Yazdani", nationl_code='123456790')


print(isinstance(ali, Account))
print(ali.__class__ == Account)
