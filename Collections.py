from collections import namedtuple, deque, ChainMap, Counter, OrderedDict, defaultdict

# collection modules
# namedtuple() -we can get the names for the values inside the tuple
a = namedtuple('technology', 'coursename, level')
s = a('python', 'basic', )

print(s)

# deque - can do insertion and deletion easily
b = ['e', 'd', 'r', 'e', 'k']
c = deque(b)
print(c)
c.appendleft('best')
print(c)

# Chainmap - merge two dictonaries
d = {1: 'good', 2: 'bad'}
e = {3: 'good1', 4: 'bad1'}
f = ChainMap(d, e)
print(f)

# Counter - it is used on the list/tuple/dictionary to get count of values/duplicated values
g = [1, 1, 1, 2, 2, 2, 3, 35, 5, 22, 7, 7, 1, 17, 7, 3]
h = Counter(g)
print(h)

# OrderedDict - it remebers the order that we used
d = OrderedDict()
d[1] = 11
d[2] = 22
d[3] = 33
print(d)
d[1] = 44  # even if we update the value which was assigned before won't be changed
print(d)

# defaultdict - doesn't throw any error even if the value is missing or not present inside the dictionary
f = defaultdict(int)
f[1] = 'GOOD'
f[2] = 'bad'
print(f[3]) # if we use normal dictionary , it will throw error but here it will give 0 as a output

#  UserDict, UserString, UserList
