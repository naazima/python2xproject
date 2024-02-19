n = 5
if n == 6:
    print("good")
else:
    print("bad")


def long_function_name(name):
    print("foo", name)


# call a function

long_function_name("naaz")


def long_function_name(a, b):
    return a * b


# call a function

res1 = long_function_name(a=5, b=10)
print("res1", res1)


# using args
def make_pizza(*topings, base):
    for topping in topings:
        print(topping, end=" ")
        print(base, end="\n")


# call a function

make_pizza("onion", "olive", base="wheat")
make_pizza("onion", base="gf")

# writing a reverse function

Original_str = input("enter a str")
reverse_str = ""
# print (reverse_str,Original_str)
for i in Original_str:
    reverse_str = i + reverse_str
print(reverse_str, end="")

