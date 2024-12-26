import array as arr


# listing
a = arr.array('i', [1, 4, 6, 7, 3])  # arr- module name, array - constructor , i - typecode, values
print(a)
print(a[2])
print(a[-4])
print("*************")

# find Length
print(len(a))
print("*************")

#  Add/update element , can use append, extend, insert
a[4] = 10
a.append(33)
# a.extend([2, 4])
# a.insert(2, 14)
print(a)
print("*************")

# remove/delete the element ,pop , remove
del (a[0])
a.remove(4)
print(a)
print("*************")

# array concatenation
array1 = arr.array('i' , [1,4,6])
array2 = arr.array('i' , [2,3,90])
result = arr.array('i')
result = (array1 + array2)
print(result)
print("*************")

# slicing
print(a)
print(a[0:3])
print("*************")

# Loop  for, while loops
print(a)
for x in a:
    print(x)
for x in a:
    print(x*2)