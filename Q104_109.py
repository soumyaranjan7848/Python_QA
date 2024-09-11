# 104 Write a program that prompts the user to specify the length of a list and then requests numbers to 
#populate that list. Display the fi nal list as the output.
length_list=int(input("Input the length of list:"))
result=[]
for i in range(0,length_list):
    number=int(input("Enter a number="))
    result.append(number)
print(result)

# 105 Create a list and prompt the user for an 'old number' followed by a 'new number.' 
#If the 'old number' exists in the list,replace it with the 'new number' provided by the user.
my_list=[23,33,45,56,15]
old_num=int(input("Enter the old number:"))
new_num=int(input("Enter the new number:"))

for i in range(0,len(my_list)):
    if my_list[i]==old_num:
        my_list[i]=new_num
    else:
        print("Number is not in the list")
print(my_list)

# 106 Remove all the even numbers from the list.
my_list = [28,20,33,77,12,11,64]
for i in my_list:
    if i % 2 == 0:
        my_list.remove(i)

print("List after removing even numbers :", my_list)


# 107 Ask the user for a number. Then, from a list of numbers, 
# remove all the numbers that can be divided by the number the user entered.
my_list=[23,34,45,56,67,78]
num=int(input("Enter a number:"))
for i in my_list:
    if i%num==0:
        my_list.remove(i)

print("remove all the numbers that can be divided by the number the user entered:",my_list)


# 108 Generate a list of at least 10 numbers. Then, create two separate lists called
# 'odd' and 'even.' Put all the odd numbers from the original list into the 'odd' list, 
# and all the even numbers into the 'even' list.

my_list=[21,34,50,36,23,45,67,84,33,94,95]
odd=[]
even=[]
for i in my_list:
    if i%2==0:
        even.append(i)
for i in my_list:
    if i%2!=0:
        odd.append(i)

print(odd)
print(even)

# 109 Start by creating two separate lists with random numbers. 
# Then, create a third list that merges the numbers from the first and second lists together.
list1=[1,2,3,4,5]
list2=[6,7,8,9,10]
#merge_list=list1+list2

merge_list=[]
for i in list1:
    merge_list.append(i)

for i in list2:
    merge_list.append(i)

print(merge_list)

















