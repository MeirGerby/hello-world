def power_of_number(n):
    def square(x):
        return x * n
    return square

power_by_three = power_of_number(3)
print(power_by_three(3))

def count():
    number = 0
    def call_counts():
        nonlocal number
        number += 1
        print(number)
    return call_counts

call = count()
call()
call()

