# Readfile data
file_path = 'test1.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()  # read all the contents of the file
        print(content)
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")

print("**************************************************************")

file_path = 'test1.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read(
            5)  # when we want to read only first few characters in the file(it reads white space as well)
        print(content)
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")

print("**************************************************************")

ile_path = 'test1.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readline()  # when we to read line by line
        print(content)
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")

print("**************************************************************")

# print line by line using readline method
# we can't use the above what if there are 100 lines i can;t rigt file.readline() 100 times in that case use this below method
# using readline method
ile_path = 'test1.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readline()
        while lines != "":
            print(lines)
            lines = file.readline()

except UnicodeDecodeError as e:
    (
        print(f"Error reading the file: {e}"))

print("**************************************************************")

# using readlines method  - difference btw above and this method is that both works the same but in this method after read all the lines will be stroed in the list so that it will be easy for u to further utilize
ile_path = 'test1.txt'

try:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        print(lines)
        print(len(lines))
        for i in lines:  # or for i  in lines
            print(i)
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")

# Write into file
print("******************** Write **********************")

# reversed the content
file_path = 'test1.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.readlines()
        print(content)
except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")
i = (len(content)) - 1
for i in range(i, -1, -1):
    print(content[i])

# read, reverse and then write
file_path = 'test1.txt'
try:
    with open(file_path, 'r', encoding='utf-8') as reader:
        content = reader.readlines()
        reversed(content)
        with open(file_path, 'w', encoding='utf-8') as writer:
            for j in reversed(content):
                writer.write(j)
except UnicodeDecodeError as e:
        print(f"Error reading the file: {e}")

except UnicodeDecodeError as e:
    print(f"Error reading the file: {e}")
