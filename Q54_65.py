#54 Ask a number from user. Print all the numbers from 1 to that number.
num=int(input("Enter the number:"))

for i in range(1,num+1):
    print(i,end=" ")

#55 Ask a number (N) from user. Print all the numbers from N to 1.
N=int(input("\nEntert the number:"))
for i in range(N,0,-1):
    print(i,end=" ")

#56 Ask start number and end number from user. Print all the numbers from start to end using for loop.
str=int(input("\nEnter the start number:"))
end=int(input("Enter the end number:"))

for i in range(str,end+1):
    print(i,end=" ")

#57 Calculate the sum of all the numbers from 1 to 10.
sum=0
for i in range(1,11):
    sum=sum+i
print("\nsum of all the numbers from 1 to 10:",sum)

#58 Calculate product of all the numbers from 1 to 10
prd=1
for i in range(1,11):
    prd=prd*i
print("\nsum of all the numbers from 1 to 10:",prd)

#59 Calculate how many numbers are divisible by 7 from 1 to 100
count=0
for i in range(1,101):
    if i%7==0:
        count=count+1
print(count)
        
#60 Calculate how many numbers are divisible by both 6 and 7 between 1 to 200.
count=0
for i in range(1,201):
    if i%6==0 and i%7==0:
        count=count+1
print(count)

#61 Write a program to calculate the sum of all the numbers divisible by 4 from 20 to 50.
sum=0
for i in range(20,51):
    if i%4==0:
        sum=sum+i
print("sum of all the numbers divisible by 4 from 20 to 50:",sum)

#62 Calculate how many numbers are divisible by 6 and 7 between 1 to 200.
count=0
for i in range(1,201):
    if i%6==0 and i%7==0:
        count=count+1
print(count)

#63 Ask a number from user. Print the multiplication table of that number.
Num=int(input("Enter the number:"))
for i in range(1,11):
    result=Num*i
    print(Num,"x",i,":",result)

#64 Calculate factorial of a number entered by user. 5!=1*2*3*4*5
Num1=int(input("Enter the number:"))
fact=1
for i in range (1,Num1+1):
        fact=fact*i
print(fact)  

#65 Ask to numbers x and y from the user. If x<y then print all the numbers from x to y, but if
#y<x then print all the numbers from y to x.
x=int(input("Entwer the 1st number:"))
y=int(input("Entwer the 2nd number:"))

if x<y:
    print("Numbers from", x, "to", y, "are:")
    for i in range(x,y+1):
        print(i)

else:
    print("Numbers from", y, "to", x, "are:")
    for i in range(y,x+1):
        print(i)
     












