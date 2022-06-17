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


funcs = []
for x in range(10):
    def some_function(x=x):
        return x


    funcs.append(some_function)

print(*[f() for f in funcs], sep='\n')
