#String operations
str1="Hello World"
str2="Welcome to Python"

#Copy
str3=str1
print("Original String:",str1)
print("Copied String:",str3)

#Concatenate
print("Concatenated string:",str1+str2)

#Substring
if "Hello" in str1:
    print("'Hello' is a substring of string str1.")
else:
    print("'Hello' is not a substring of string str1.")

#Equal
if (str1==str2):
    print("String 1 & 2 are equal.")
else:
    print("String 1 & 2 are not equal.")

#reverse
print("Original string 1:",str1)
print("Reversed string 1:",str1[::-1])

#length
print("length of string 1:",len(str1))
print("length of string 2:",len(str2))

'''
# String operations
#Copy
str1="Hello"
str2=str1
print("String1:",str1)
print("String2:",str2)

#Concatenate
str1="Hello"
str2="World"
print("Concatenated string:",str1+str2)

#Substring
str3="Computer Science"
if "Computer" in str3:
    print("'Computer' is a substring of string str3.")
else:
    print("'Computer' is not a substring of string str3.")

# Equal
str1="High"
str2="High..."
if (str1==str2):
    print("String 1 & 2 are equal.")
else:
    print("String 1 & 2 are not equal.")

#reverse
str1="Hello"
print("Original string:",str1)
print("Reversed string:",str1[::-1])

#length
str1="Magnificient"
print("length of string:",len(str1))

'''