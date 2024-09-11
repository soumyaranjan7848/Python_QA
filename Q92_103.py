# 92 Make your own list. Print the list in reverse.
my_list=[23,45,"soumya",-22.34,True]
print(my_list[::-1])
# OR 
my_list=[23,45,"soumya",-22.34,True]
for i in range(len(my_list)-1,-1,-1):
    print(my_list[i])


# 93 Make your own list. Print all the even numbers present in the list.
my_list=[32,33,44,55,66,77,88]
for i in my_list:
    if i%2==0:
        print(i)

# 94 Make your own list. Print all the odd numbers present in the list.
my_list1=[3,34,45,66,77,67,88]
for i in my_list1:
    if i%2!=0:
        print(i,end=" ")
print()
# 95 Make your own list. Print all the elements present at even index position.
my_list=[23,45,56,66,"Soumya",-23,True,44]
for i in range(0,len(my_list)):
    if i%2==0:
        print(my_list[i])

# 96 Make your own list. Print the sum of all elements present in that list
my_list=[23,3,4,5,22,24,24]
sum=0
for i in my_list:
    sum=sum+i
print("The sum is : ",sum)

# 97 Make your own list. Count the number of even numbers present in that list.
my_list=[2,3,5,12,24,33,55]
count=0
for i in my_list:
    if i%2==0:
        count=count+1
print("No. of even number is :",count)
        
# 98 Make your own list. Count how many numbers are divisible by both 2 and 5 in that list.
my_list=[2,3,5,12,10,24,33,55]
count=0
for i in my_list:
    if i%2==0 and i%5==0:
        count=count+1
print("No. are divisible by both 2 and 5 in that list is :",count)

# 99 Make your own list. Find the sum of all even numbers present in that list.
my_list=[2,3,5,12,10,24,33,55]
count=0
for i in my_list:
    if i%2==0:
        count=count+i
print("sum of all even numbers present in that list is :",count)

# 100 Make your own list. Find the sum of all numbers divisible by 3 or 4.
my_list=[2,3,5,12,10,24,33,55]
count=0
for i in my_list:
    if i%3==0 and i%4==0:
        count=count+i
print("sum of all numbers divisible by 3 or 4 is :",count)

# 101 Make your own list. Print how many positive and negative numbers are here.
my_list=[2,-3,5,-12,10,24,-33]
positive=0
negative=0
for i in my_list:
    if i>0:
        positive=positive+1
    if  i<0:
        negative=negative+1
print("Positive number are :",positive) 
print("Negative number are :",negative) 

# 102 Make your own list. Print the largest number present in that list.
my_list=[28,377,576,123,10,274]
#print(max(my_list))
largest=0
for i in range(0,len(my_list)):
    if my_list[i] > largest:
        largest=my_list[i]
print("largest number is :",largest)


# 103 Make your own list. Print the smallest number present in that list.
my_list=[28,377,576,123,10,274]
#print(min(my_list))
smallest=my_list[0]
for i in range(0,len(my_list)):
    if my_list[i] < smallest:
        smallest=my_list[i]
print("smallest number is :",smallest)













































