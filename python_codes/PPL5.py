'''# 5.a
input_list=['MIT', 'SOE', 'MIT' , 'ADTU', 'ADT', 'Loni', 'Design', 'Food', 'Technology']
count_mit=input_list.count("MIT")
count_adt=input_list.count("ADT")
if count_mit==2 and count_adt>=1:
    print("condition satisfied")
else:
    print("condition not satisfied")

# 5.b
print("Case 1")
inp_list=[100,35,23,100,45,89,90]
count1=inp_list.count(100)
count2=inp_list.count(90)
if count1==2 and count2>=2:
    print("condition satisfied")
else:
    print("condition not satisfied")
print()

print("Case 2")
inp_list2=[90,110,130,150,170,200,200]
count1=inp_list2.count(200)
count2=inp_list2.count(130)
if count1>=2 and count2==1:
    print("condition satisfied")
else:
    print('condition not satisfied')


# 5.c
l=[]
n=int(input("Size of list:"))
for i in range(0,n):
    ele=int(input("enter element:"))
    l.append(ele)
print(l)
count_third=l.count(l[2])
if len(l)>10 and count_third==2:
    print("condition satisfied")
else:
    print("condition not satisfied")
  
'''
# 5.d
l=[3,10,2,5,7,4,1,8,6,9]
print("Original List:",l)
l.sort()
print("Sorted List:",l)


#l.sort(reverse=True)
#print(l)


 


'''
l=[1,2,3]
print(l)
ele=int(input("enter element:")) # ele = 5
l.append(ele) # listname.append(element)
print(l)
ele=int(input("enter element:")) 
l.append(ele) # listname.append(element)
print(l)'''
'''l=[]
#n=int(input("Size of list:"))
while True:
    ch=input("Enter element yes or no:")
    if ch=='y':
        ele=int(input("enter element:"))
        l.append(ele)
    elif ch=='n':
        break
    else:
        print("wrong choice")
    
print(l)
count_third=l.count(l[2])
if len(l)>10 and count_third==2:
    print("condition satisfied")
else:
    print("condition not satisfied")'''
