'''# 6c
# Add a new movie
dict1={}
n=int(input("enter no. of movies showing in cinema:"))
for x in range(0,n):
    mov=input("enter movie name:")
    time=int(input("enter time:"))
    dict1[mov]=time

print(dict1)
print()

# Display movies available at 9 pm
print("Movies showing at 9 PM:")
for x in dict1:
    if dict1[x]==9 :
        print(x)
print()

# Remove the details of the specific movie
rem=input("Enter movie to be deleted:")
dict1.pop(rem)
print(dict1)

# Removes the last movie details
dict1.popitem()
print(dict1)


# method - 2
d={}
d["Thor"]=7
d["Rufus"]=9
d["Vikram"]=8
d["Shock"]=9
print(d)

print("Movies at 9 pm")
for i in d:
    if d[i]==9:
        print(i)

d.pop("Rufus")
print(d)
d.popitem()
print(d)

'''
'''
#6a
d={}
l1=[1,2,3]
l2=['a','b','c']
for i in range(len(l1)):
    d[l1[i]]=l2[i]

print(d)

# method -2
l1=[1,2,3]
l2=['a','b','c']
d=dict(zip(l1,l2))
print(d)


#6b
d={}
for i in range(1,10):
    d[i]=i**2

print(d)

# method - 2
l=[1,2,3,4,5]
for i in l:
    d[l]=l**2

print(d)
'''

'''
# 6.a
l1=[1,2,3]
l2=['a','b','c']
d=dict(zip(l1,l2))
print(d)


# 6.b
d={}
l=[1,2,3,4,5]
for i in l:
    d[i]=i**2

print(d)

'''
# 6.c
# Add a new movie
d={}
d["Thor"]=7
d["Rufus"]=9
d["Vikram"]=8
d["Shock"]=9
print(d)
print()

# Display movies available at 9 pm
print("Movies at 9 pm :-")
for i in d:
    if d[i]==9:
        print(i)
print()

# Remove the details of the specific movie
d.pop("Rufus")
print(d)
print()

# Removes the last movie details
d.popitem()
print(d)


