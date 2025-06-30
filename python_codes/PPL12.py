print("Question 1")
a=5
b=0
try:
    print("The result of division is : ", a/b)
except ZeroDivisionError:
    print("Division by 0 is not allowed")


print("Question 2")
try:
    open('new.txt','r')
#except FileNotFoundError:
#    print("File does not exist")

except :
    print("Error.........")
    
print("Question 3")
list1=[1,2,3,'animus']
try:
    print("The sixth value is : ", list1[6])
except IndexError:
    print("The index is out of range")


print("Question 4")
x=8
y='d'
try:
    print("The addition is : ", x+y)
except TypeError:
    print("The values are of different types")


except :
    print("Error.........")