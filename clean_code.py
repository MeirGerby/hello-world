def calculating_speed_and_rate(a, b):
    return a / (b * 60)
print(calculating_speed_and_rate(120, 2))


def calculate_the_area_of_circle(r):
    return 3.14159 * r * r
print(calculate_the_area_of_circle(5))

def print_user(name, age):
    print("User:", name)
    print("Age:", age)



def process_user(name, age):

    print("User:", name)
    checking_age(age)

def checking_age(age):

    if age < 18:
        print("Minor")
    else:
        print("Adult")
    if age >= 65:
        print("Senior")


def add_numbers(x,y):
    return x+y
print(add_numbers(2,3))