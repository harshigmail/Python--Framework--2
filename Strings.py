str2 = "Rahulshetty"
str1 = "consulting firm"
a = 10
str3 = "firm"

print(str2)
print(str2[2])  # print character
print(str2 + str1)  # concatenate two strings
print(str2[5:11])  # print in between text

# concatenate two different datatypes , int and string
r1 = str2 + str(a)
print(r1)
# or
r2 = "{}{}".format(str2, a)
print(r2)

print(str3 in str1)   # sub string check
print(str2. split("e"))  # to split the words
str4 = "  gre ate  "
print(str4)
print(str4.strip())  # to remove the white space at the end and the beginning of the word
print(str4.lstrip())
print(str4.rstrip())
