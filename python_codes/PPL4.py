'''# 4.a
min=int(input("Enter lower limit:"))
max=int(input("Enter upper limit:"))
count=0
for i in range(min,max+1):
    if (i%5==0 and i%9==0):
        print(i," is divisible by 5 and multiple of 9.")
        count=count+1
    else:
        continue

if (count==0):
    print("No numbers are divisible by 5 and multiple of 9")

'''
#4.b
l=[1,2,3,4,5,6]
c_even=0
c_odd=0
c_prime=0
for i in range(len(l)):
    x=l[i]
    count=0
    # Prime no.
    if (x>1):
        for j in range(2,x+1):
            if (x%j==0):
                count=count+1
            else:
                continue
    if (count==1):
        c_prime=c_prime+1       # Counting Prime no
        if (x%2==0):            # Check even or odd
            print(x,"is a prime no. as well as even no.")
            c_even=c_even+1     # Counting Even no
        else:
            print(x,"is a prime no. as well as odd no.")
            c_odd=c_odd+1       # Counting Odd no
    else:
        if (x%2==0):            # Check even or odd
            print(x,"is not a prime no. but an even no.")
            c_even=c_even+1     # Counting Even no
        else:
            print(x,"is not a prime no. but an odd no.")
            c_odd=c_odd+1       # Counting Odd no
            
print("Total no. of prime no.:",c_prime)
print("Total no. of even no.:",c_even)
print("Total no. of odd no.:",c_odd)


 

        




