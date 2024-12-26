# if else loop
greeting = "Good morning"

if greeting == "morning":
    print("condition is matched")
else:
    print("condition do not matched")

print("code completed")

# for loop
obj = [1, 2, 3, 4, 5]
for i in obj:
    print(i)

# Multiple of 2
obj = [1, 2, 3, 4, 5]
for i in obj:
    print(i * 2)

for i in range(1, 6):
    print(i * 2)

# Sum of natural numbers(1 to 5)
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

# for(i=1, i<6 , i+2) how to do this i++/i--
for k in range(1, 6, 2):
    print(k)

for k in range(6, 1, -2):
    print(k)

print("** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *")
# if the starting index is not given in that case the loop will starts from 0 i.e, 0-6 will print
for k in range(7):
    print(k)

# While loop
print("** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *")
# infinite loop
# man = 4
# while man > 1:
# print(man)

# finite loop
man = 4
while man > 1:
    print(man)
    man = man - 1

# i want only 4 and 2 to be printed
man = 4
while man > 1:
    print(man)
    man = man - 2
# or
man = 4
while man > 1:
    if man != 3:
        print(man)
    man = man - 1

# break
man = 4
while man > 1:
    if man == 2:
        break
    print(man)
    man = man - 1

# Continue
print("** ** ** ** ** ** ** ** ** ** ** ** ** ** ** ** *")
man = 4
while man > 1:
    if man == 3:
        man = man - 1
        continue
    if man == 1:
        break
    print(man)
    man = man - 1


print("**************")
count = 1
while count<14:
    if count>10:
    print("Numbe is too small")
    elif count<15
    print("Numbe is too large")
while count==13:
    print("yoou made it")

