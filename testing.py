# largest
from math import factorial

nums = [10, 8, 5, 3]

for num in nums:
    largest = nums[0]
    if num > largest:
        largest = num


print(largest)

# factorial
num2 = 5
fact = factorial(num2)
print(fact)


# or
def fact(n):
    if n== 0:
        return 1
    else:
        return n * fact(n-1)


num2 = 5
result = fact(num2)
print(result)

# palindrome
str = ['m', 'a', 'd', 'e', 'm']
new = []
a = (len(str))
b = a-1

for i in str:
    if i == str[b]:
        new.append(i)
        b = b-1
    else:
        print("Not a palindromw")

if new == str:
    print("Is palindrome")

# reverse string
str = " Hello world"
str1= ""
for char in str:
    str1 = char + str1
print(str1)

