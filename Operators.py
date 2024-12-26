x = 10
y = 6
# arithmetic operator
print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)
print("**************")

# Logical operator
if x == y:
    print("equal")
elif x > y:
    print("greater")
else:
    print("smaller")
print("**************")

if (x < y) and (x > 9):
    print("correct")
else:
    print('not correct')

if (x < y) or (x > 9):
    print("correct")
else:
    print('not correct')

# Identify operator
list1 = [1, 2, 3]
list2 = [1, 2, 3]
x = list1
print(x is list1)
print(list1 is list2)
print("**************")

# membership operator
print(x in list1)
print(1 in list2)
print("**************")

# bitwise operator
x = 10
print(x)
print(y)
print(x & y)
print(x | y)
print(x ^ y)
# print(x ~ y)
print(x << y)
print(x >> y)
