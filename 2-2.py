# Loop :

#  -  pass
#  -  continue
#  -  break

# While
# while True:
#     number = int(input("Enter your mark : "))
#
#     if number < 0 or number > 20:
#         print("Error: Enter a valid number!")
#         continue
#     print("Your mark saved!")
#     break

#  For
# for i in [56, 34, 23, 1, 453, 2, 5]:
#     print(i)

data = int(input("Enter a number : "))
# print("+" if data > 0 else "-")
print("+" if data > 0 else "0" if data == 0 else "-")
