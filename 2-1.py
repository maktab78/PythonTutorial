data = "hello world!"

# len

len(data)

# Slice
# [ start = 0 : stop = len : step = 1 ]
print(data[:])
print(data[::-1])
print(data[4:][::-1][-4:-9:-1])
# Step1 : o world!
# Step2 : !dlrow o
# Step3 : orld!

resume = """
    Hi , am abolfazl
    age : 21
    live in Tehran
"""

# print(resume)
data = "Salam 78"
print(data[:-2], str(int(data[-2:]) + 100), sep=" -- ", end=" ||| ")
print(data[::-3])
print("Akbar" * 4)

# string method:
print(data.count("a"))
ifirst_a = data.index("a")
print(data[:ifirst_a] + 'B' + data[ifirst_a + 1:])
print(data.replace('a', 'B', 1))
print(data[::-1].replace('a', 'B', 1)[::-1])

data = "Be isfahan ro ke ta"
# print(data.title())
# print(data.split("ro"))
print(data.casefold())
print(data.lower())

# True - False
print(data.isalpha())
print("reza" not in data)

# List
data_list = [True, 45353, "Hello world", 64.34, None, "Hello world"]

data_list.append(False)

print(data_list)
print(data_list[-1])

print(data_list.count("Hello world"))
data_list.append(["a", "b", "c", "d"])
print(data_list)

li = [10, -5 ,8 ,23]
print(li)
# print(li.sort())
print(sorted(li)) # in-place func
print(li)

data_list.extend(["a", "b", "c", "d"])
print(*data_list, sep=" || ")

