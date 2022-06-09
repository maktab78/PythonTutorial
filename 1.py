# Types:
#  - int
number = 23233333

#  - float
pi = 3.1415

#  - string
name = "Akbar"

#  - boolean
isActive = False

#  - None type
flag = None

# Dynamic type:
number_str = str(number)  # "23233333"

# type:
# print(type(number_str))

# i / o
# number = float(input("Enter a number : "))
# print(type(number))  # str

# Ml String
banner = """
 ____        _                 
/ ___|  __ _| | __ _ _ __ ___  
\___ \ / _` | |/ _` | '_ ` _ \\
 ___) | (_| | | (_| | | | | | |
|____/ \__,_|_|\__,_|_| |_| |_|
                            
"""

# print(banner)


# Condition
n = int(input("enter a number : ".capitalize()))

if n > 0:
    print("Enter +")
    print("+++++++++++++")
elif n < 0:
    print("Enter -")
    print("-------------")
else:
    print("Enter 0")
    print("0000000000000")

if type(n) == int:
    print('Int')

    if n > 0:
        print("Enter +")
        print("+++++++++++++")
    if n < 0:
        print("Enter -")
        print("-------------")
    if n == 0:
        print("Enter 0")
        print("0000000000000")


