# 110 Make a list of your own. And remove all the duplicates element from that list.
my_list=[2,3,4,2,14,2,5,3]
print("Original List: ", my_list)
result=[]
for i in range(0,len(my_list)):
    if (my_list[i]) not in result:
        result.append(my_list[i])
print("List after removing Duplicates: ",result)

# 111 Make a list. Then ask a number from user. If number exists in that list then print the 
# position of the element else print -1.
my_list=[23,34,4,55,66,2,4,5,5]
num=int(input("Enter the number:"))
for i in my_list:
    if num==i:
        p=my_list.index(i)
        print("Number is present",p)
        break
else:
    print("Number is not present: -1")

# 112 Take 10 integer inputs from user and store them in a list. Now, copy all the elements in another
# list but in reverse order.
length_list=int(input("Input the length of list:"))
my_list=[]
for i in range(0,length_list):
    number=int(input("Enter a number="))
    my_list.append(number)
print(my_list)
new_list=[]
for i in reversed(my_list):
    new_list.append(i)
print(new_list)


# 113 Write a program to fi nd the average of all the numbers present in the list.
my_list=[2,5,6,3,7,8,2]
sum=0
count=0 
for i in my_list:
    sum+=i
    count+=1
average=sum/count
print("Average of the numbers in the list is :",average)


# 114 Write a Python code to find the occurrence of each element in a list and 
# print the element with the highest occurrence.
my_list=[2,4,6,9,3,12,65,4,7,4]
result=[]

for i in my_list:
    if i not in result:
        result.append(i)

highest_occ_element=0
highest_occurrence=0

for i in result:
    c=result.count(i)
    print(i,"occer",c,"times.")
    if c>highest_occurrence:
        highest_occurrence=c
        highest_occ_element=i


print("The element with the highest occurrence is : ",highest_occ_element)
  
# 115 Write a program that has two lists and make a new list that contains only the 
# common elements between them without duplicates.
my_list1=[3,2,2,4,9,7,5]
my_list2=[2,2,4,5,8,8,7,9]
new_list=[]
for i in my_list1:
    for j in my_list2:
        if i==j and i not in new_list:
            new_list.append(i)

print("Common elements are : ",new_list)

# 116 Write a Python code to find the second largest element in a list without sorting.
my_list=[2,32,24,45,12,23]
largest=float("-inf")
second_largest=float("-inf")

for i in my_list:
    if i>largest:
        second_largest=largest
        largest=i
    elif i>second_largest and i<largest:
        second_largest=i

print("2nd largest:",second_largest)


# 117 Make a program that takes a list of integers and returns the product of all the elements.
my_list=[2,4,5,6,7,2]
product=1
for i in my_list:
        product=i*product

print(product)


# 118 Write a program to find and print all prime numbers within a given list.
my_list=[2,3,5,6,7,9,11,13]

for i in my_list:
    factor=0
    for j in range(1,i+1):
        if i%j==0:
            factor=factor+1
    if factor==2:    
        print(i)

# 119 Write a program to split a given list into two halves.
my_list=[2,4,5,6,7,8,9,3,8,2]
n=len(my_list)
mid=n//2
first_half=my_list[:mid]
second_half=my_list[mid:]
print(first_half)
print(second_half)

# 220 Write a program that swaps the first and last elements of a given list
my_list=[2,4,5,6,7,23]
last=my_list[-1]
first=my_list[0]
my_list[0],my_list[-1]=my_list[-1],my_list[0]
print(my_list)




























