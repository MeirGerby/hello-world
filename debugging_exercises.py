def triangle(height):
    """
    this function takes number from the user and print a matrix
    """
    for i in range(1, height + 1):
        for j in range(1, height + 1):
            print(f"{i * j:4}" , end="")
        print()


def raise_numbers(height):
    """
    the number that taken would be return by a triangle numbers
    """
    for i in range(1, height + 1):
        for j in range(1,i + 1):
            print(f"{j:3}", end="")
        print()

def greet(username):
    print("the user name was not defined")
    return f"Hello, {username}!"

print(greet("meir"))

# counts = {"a":1, "b":2, "c":3}
# for k in counts:
#     if counts[k] % 2 == 1:
#         del counts[k]
#
# print(counts)
print("the problem is because of the dictionary changed during the iteration")
counts = {"a":1, "b":2, "c":3}
counts1 = {}
for k in counts:
    if counts[k] % 2 != 1:
        counts1[k] = counts[k]

print(counts)

# text = "debugging"
# print(text.push("!"))
print('this method is not for string')

text = "debugging"
text1 = text + "!"
print(text1)

# nums = [1, 2, 3]
# for i in range(0, len(nums)):
#     print(nums[i + 1])
print("the index is out of range")

nums = [1, 2, 3]
for i in range(0, len(nums)):
    print(nums[i])


# config = {"host": "localhost", "port": 5432}
# print(config["username"])

print("the key is not defined")

config = {"host": "localhost", "port": 5432}
if "username" in config:
    print(config["username"])
else:
    print("key not found")

# age = "12"
# print(age + 5)

print("adding incompatible types ")

age = 12
print(age + 5)


# user_input = "12.5"
# print(int(user_input))

print("bad int conversion")

user_input = "12.5"
print(float(user_input))

# def ratio(a, b):
#     return a / b
# print(ratio(10, 0))

print("ZeroDivisionError – unchecked divisor")

def ratio(a, b):
    return a / b
print(ratio(10, 4))


# import jsonn
# print(json.dumps({"ok": True}))

print("ImportError / ModuleNotFoundError – misspelled import")
import json
print(json.dumps({"ok": True}))



# def down(n):
#     return down(n - 1)
# print(down(5))

print("RecursionError – missing base case")
def down(n):
    if n == 1:
        return None
    else:
        return down(n - 1)
print(down(5))


# x = 5
# while x > 0:
#     print(x)
# x never changes

print("Infinite loop – loop condition never changes")
x = 5
while x > 0:
    x -= 1
    print(x)
# x never changes


# def add_item(item, bucket=[]):
#     bucket.append(item)
#     return bucket
# print(add_item("a"))
# print(add_item("b"))

print("Mutable default argument – state “leaks” across calls")
def add_item(item, bucket=None):
    if bucket is None:
        bucket = []
    bucket.append(item)
    return bucket
print(add_item("a"))
print(add_item("b"))


# funcs = []
# for i in range(3):
#     funcs.append(i)
# for f in funcs:
#     print(f)
print("Late binding in closures – all functions print same value")

funcs = []
for i in range(3):
    funcs.append(lambda i = i: print(i))
for f in funcs:
    f()

# items = [1, 2, 3, 4, 5]
# for x in items:
#     if x % 2 == 0:
#         items.remove(x)
# print(items)

print("changing the list in iterable operation ")

items = [1, 2, 3, 4, 5]
item = []
for x in items:
    if not x % 2 == 0:
        item.append(x)
print(item)

# a = [1, 4, 9]
# b = [2, 3, 6, 8]
# i, j = 0, 0
# merged = []
# while i < len(a) and j < len(b):
#     if a[i] < b[j]:
#         merged.append(a[i])
#         i += 1
#     else:
#         merged.append(b[j])
#         j += 1
# print(merged)

a = [1, 4, 9]
b = [2, 3, 6, 8]
i, j = 0, 0
merged = []
while i < len(a) and j < len(b):
    if a[i] < b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged += a[i: len(a)]
merged += b[j: len(b)]
print(merged)

print("the last item was not appended")

# import logging
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("Start")


# for i in range(3):
#     j = 0
#     j += 1
#     print(j)

print("the varyable is not change ")
for i in range(3):
    j = i
    j += 1
    print(j)

# name = "Avi"
# print(f"User: {full_name}")
print("the varyable is not defined")

name = "Avi"
print(f"User: {name}")


# data = [10, 20, 30, 40]
# total = 0
# for i in range(len(data) - 1):
#     total += data[i]
# print("Total:", total)

print("the last value is missing ")

data = [10, 20, 30, 40]
total = 0
for i in range(len(data)):
    total += data[i]
print("Total:", total)



