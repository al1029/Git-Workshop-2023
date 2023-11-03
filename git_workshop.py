import math

# all functions should take in a numerical value and return a numerical value
# rename your function
def func1(num_a):
    return (5 + num_a)

def func2(num_b):
    return (7 + num_b)

# both people should modify this function
def func3(num_a, num_b):
    print(f"This is the first magical number: {func1(num_a)}" )
    print(f"This is the second magical number: {func2(num_b)}")

a = 1
b = 1
x = func1(a)
y = func2(b)
func3(x, y)
