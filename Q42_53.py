"""
# Print 1-10 using while loop
i=1
while i<=10:
    print(i,end=" ")
    i=i+1
print("This is Done")

# print 1 to 20 , only even number 
i=1
while i<=20:
    if i%2==0:
        print( i)
    i=i+1

"""
#42 Ask a number from user. Print all the numbers from 1 to that number
n=int(input("Enter the number:"))
i=1
while i<=n:
    print(i)
    i=i+1

#43 Ask a number N from user. Print all the numbers from N to 1
N=int(input("Enter the number:"))
while N>=1:
    print(N)
    N=N-1

#44 Ask start number and end number from user. Print all the numbers from start to end using while loop.
str=int(input("Enter the starting number:"))
end=int(input("Enter the ending number:"))
if str>end:
    print("Starting number is lessthan ending number")
else:
    while str<=end:
        print(str)
        str=str+1

#45 Calculate the sum of all the numbers from 1 to 10.
i=1
sum=0
while i<=10:
    sum=sum+i
    i=i+1
print("Sum of 1 to 10 number is :",sum)

#46 Calculate product of all the numbers from 1 to 10.
i=1
prd=1
while i<=10:
    prd=prd*i
    i=i+1
print("Product of 1 to 10 number is :",prd)


#47 Calculate how many numbers are divisible by 7 from 1 to 100.
i=1
count=0
while i<=100:
    if i%7==0:
        count=count+1
    i=i+1
print(count)

#48 Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
i=1
count=0
while i<=200:
    if i%7==0 and i%6==0:
        count=count+1
    i=i+1
print(count)

#49 Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.
i=20
sum=0
while i<=50:
    if i%4==0:
        sum=sum+i
    i=i+1
print("sum of all the numbers divisible by 4 from 20 to 50 is :",sum)

#50 Calculate how many numbers are divisible by 6 and 7 between 1 to 200.
i=1
count=0
while i<=200:
    if i%6==0 and i%7==0:
        count=count+1
    i=i+1
print(count)

#51 Ask a number from user. Print the multiplication table of that number.
n=int(input("Enter the number:"))
count=1
while count<=10:
    result=n*count
    print(n,"x",count,":",result)
    count=count+1

#52 Calculate factorial of a number entered by user.5!=1*2*3*4*5
num=int(input("Enter the number:"))
i=1
while num>0:
    i=i*num
    num=num-1
print(i)

#53 Ask to numbers x and y from the user. If x<y then print all the numbers from x to y, but if
#y<x then print all the numbers from y to x.

x=int(input("Entwer the 1st number:"))
y=int(input("Entwer the 2nd number:"))

if x<y:
    print("Numbers from", x, "to", y, "are:")
    while x<=y:
        print(x)
        x=x+1

else:
    print("Numbers from", y, "to", x, "are:")
    while y<=x:
        print(x)
        y=y+1






















































