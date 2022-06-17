# for x in range(10):
#     print(x)
#     x = 10

# results = []
# funcs = []

# for i in range(10):
#     def some_function():
#         return 2 ** i
#
#
#     funcs.append(some_function)
#     results.append(some_function())

# print(*funcs, sep='\n')

# result_funcs = [function() for function in funcs]

# print(*result_funcs, sep='\n')

# print(*results, sep='\n')


# funcs = [lambda: 2 ** i for i in range(10)]
# print(*funcs, sep="\n")
#
# print(*[f() for f in funcs], sep="\n")


# print(all([False, False, True]))  # False -> bool(F and F and F)
# print(any([False, False, True]))  # True -> bool(F or F or T)


# print(all([]))  # True
# print(all([[]]))  # False
# print(all([[[]]]))  # True
# print(all([[[[]]]]))  # True


def my_all(iterable):
    for element in iterable:
        if not element:
            return False
    return True


print(my_all([]))  # True -> False
print(my_all([[]]))  # False
print(my_all([[[]]]))  # True
print(my_all([[[[]]]]))  # True


