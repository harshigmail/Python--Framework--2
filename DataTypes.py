a = 3
print(a)

str = 'Good'
print(str)

b, c, d = 2, 2.4, "Team"
print(c, b, d)

#print("value is"+ c)
print("{} {}".format("value is", c))  #concatinate two different datatypes

#to know the type
print(type(c))

#List datatype - not immutable - we can modify even after create - uses []
values = [1, 'team', 3.4, 4, 100 + 3j]
# to print values
print(values[0])  #to print 1st value
print(values[2])  #to print 3rd value
print(values[-1])  #to print last value
print(values[1:4])  #to print sub values
# to insert value new value
values.insert(4, "work")
print(values)
# to add new value at last
values.append(80.4)
print(values)
# to update value
values[2] = "team team"
# to delete the value
del values[3]
print(values)


# Tuple datatype - immutable - once it is created we can't modify it - uses ()
val = [1, 'teamtuple', 3.4, 4, 100 + 3j]
# to print values
print(val[0])  # to print 1st value

val.insert(4, "work")
print(val)
val.append(80.4)
print(val)
del val[3]
print(val)



# Dictonary - uses {}
dic = {1: "team", 2: 3, "a": 4, "b": "work"}  # key / value is in string then use quotes
print(dic)
print(dic["a"])
print(dic[1])


# in python next line won't pprint if anything fails in the previous line


