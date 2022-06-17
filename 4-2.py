# from string import ascii_lowercase as a_z
#
# # results = { 'a':'A', 'b':'B', ... }
#
# # alphabet = {}
# # for char in a_z:
# #     alphabet[char] = char.upper()
#
# alphabet = {char: char.upper() for char in a_z}
#
# print(*alphabet.items(), sep='\n')


# funcs = []
# for x in range(10):
#     def some_function(x=x):
#         return x
#
#
#     funcs.append(some_function)
#
# print(*[f() for f in funcs], sep='\n')


# from ... import ...

# def hello(name):
#     print(f'Hi There!, i am {name}')
#
#     if name == "reza":
#         return True
#
#
# list(map(hello, ['ali', 'reza', 'kian', 'amir', 'hasan']))
#
# print("--------------------------------------------")
#
# any(map(hello, ['ali', 'reza', 'kian', 'amir', 'hasan']))

# All -> (...) -> True


from functools import reduce

l1 = [1, 3, 5, 7, 9]
l2 = [9, 7, 5, 3, 1]
a = reduce(lambda x, y: x + [y], l1, [10])
print(a)

fib = lambda n: reduce(lambda x, _: x + [x[-1] + x[-2]],
                       range(n - 2), [0, 1])
print(fib(20))

hi = lambda: print('Hello world')


hi()
hi()
hi()
hi()
hi()
hi()
