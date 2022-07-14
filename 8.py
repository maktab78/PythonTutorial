class Human:
    __COUNTER: int = 0

    # HUMANS = []

    def __init__(self, name: str, age: int):
        # self.__class__.HUMANS.append(self)
        self.__class__.__COUNTER += 1
        self.name = name
        self.age = age

    @classmethod
    def get_counter(cls):
        return cls.__COUNTER


reza = Human('reza', 22)
ali = Human('ali', 22)
mohammad = Human('mohammad', 22)
akbar = Human('akbar', 22)

print(Human.get_counter())


# print(Human.HUMANS)
# print(Human.HUMANS[0])


class Staff(Human):

    def __init__(self, name: str, age: int, staff_id: int):
        super().__init__(name, age)
        self.staff_id = staff_id


class Book:
    pass


class Category:
    pass


class Cage:
    pass


class Library:

    # aggregation
    def __init__(self, staff) -> None:
        self.staff = staff

    # composition
    # def __init__(self, name, age, staff_id):
    #     self.staff = Staff(name, age, staff_id)


mr_alizade = Staff('alizade', 34, 2323452342)
print(mr_alizade.staff_id)


central_lib = Library(mr_alizade)

print(central_lib.staff.name)
del central_lib

private_lib = Library(mr_alizade)
