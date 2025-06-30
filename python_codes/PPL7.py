# find the Max of three numbers
'''
def max(a,b,c):
    if (a>=b and a>=c):
        print(a,"is the biggest number.")
    elif (b>=c):
        print(b,"is the biggest number. ")
    else:
        print(c,"is the biggest number.")

a,b,c=[int(x) for x in input("Enter three numbers:").split()]
max(a,b,c)


# multiply all the numbers in a list
def mul(l):
    t=1
    for i in l:
        t=t*i
    
    return t


l=[1,2,3,4,5]
print("Total:",mul(l))

# create a list of all even numbers between 19 and 88
def newlist(l):
    for i in range(19,89):
        if (i%2==0):
            l.append(i)
        
    print("Newlist:",l)


l=[]
newlist(l)

'''
# display the current date and time and get the Python version
from datetime import datetime
import sys

def display():
    x=datetime.now()
    print("Date and Time:",x)
    print("Python Version :-")
    print(sys.version)
    print("Version info. :-")
    print(sys.version_info)

display()



