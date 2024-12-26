# without parameters
def hello():
    print(" hello")


hello()


# parameterized function
def man(name):
    print(" hello" + name)


man("gokul")


# call function inside function
def man(name):
    print(" hello" + name)


def template(a, b):
    print(a + b)


template(2, 3)

man("gokul")


# using return statement
def template1(a, b):
    return a + b


print(template1(2, 3))
