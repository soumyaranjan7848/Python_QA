#27 Write a program to check if the number is ODD, EVEN or Equal to Zero.
n=int(input("Enter the number :"))

if n==0:
    print("Number is equal to ZERO")

elif n%2==0:
   print("Number is even i.e :",n)

else:
     print("Number is odd i.e :",n)
    

#28 Write a program to check if number is divisible by 2 and 3 but not 8.
n=int(input("Enter the number :"))

if n%2==0 and n%3==0 and n%8!=0:
    print("Number is divisible by 2 and 3 but not 8 i.e :",n)
else:
    print("NO")

#29 Write a program to print the last digit of a number. (NOT A IF ELSE QUESTION)
n=int(input("Enter the number :"))
last_digit=n%10
print("The last digit of ",n,"is :",last_digit)

#30 Write a program to check if the last digit of a number is divisible by 5 or not.
n=int(input("Enter the number :"))
last_digit=n%10
if last_digit%5==0:
    print("Last digit is divisible 5")
else:
    print("Last digit is not divisible 5")
    
#31 
"""
Write a program to calculate bill. Ask the fi nal amount from the user.
You have to give discount and print the fi nal bill after discount.
50000 above - 30% discount
40000 - 49999 - 25% discount
30000 - 39999 - 20% discount
10000 - 29999 - 10% discount
1 - 9999 - No discount
Print the discount and the final amount to be paid.
"""
bill=int(input("Enter the bill amount :"))
if bill>=50000:
    discount=(30/100)*bill
    print("You got 30%\ discount")
    print("Your final bill is Rs.",discount)

elif 40000<=bill<=49999:
    discount=(25/100)*bill
    print("You got 25%\ discount")
    print("Your final bill is Rs.",discount)

elif 30000<=bill<=39999:
    discount=(20/100)*bill
    print("You got 20%\ discount")
    print("Your final bill is Rs.",discount)

elif 10000<=bill<=29999:
    discount=(10/100)*bill
    print("You got 10%\ discount")
    print("Your final bill is Rs.",discount)

else:
    print("You have no discount")
    print("Your final bill is Rs.",bill)

#32 Ask 4 numbers from user. Make sure all the numbers entered by user are different.
# Print which number is the smallest.
n1=int(input("Enter the 1st number :"))
n2=int(input("Enter the 2nd number :"))
n3=int(input("Enter the 3rd number :"))
n4=int(input("Enter the 4th number :"))

if n1<n2 and n1<n3 and n1<n4:
    print("n1 is the smallest ")
elif n2<n1 and n2<n3 and n2<n4:
    print("n2 is the smallest ")
elif n3<n1 and n3<n2 and n3<n4:
    print("n3 is the smallest ")
else:
    print("n4 is the smallest ")

#33
"""
Ask a number from user
Print “Fizz” if the number is divisible by 3.
Print “Buzz” if the number is divisible by 5.
Print “FizzBuzz” if the number is divisible by 3 and 5.
Print the number itself if none of the conditions are true.
"""
num=int(input("Enter the number:"))
if num%3==0 and num%5==0:
    print("FizzBuzz")
elif num%5==0:
    print("Buzz")
elif num%3==0:
    print("Fizz")
else:
    print("The number itselt i.e:",num)

#34 
"""
A student will not be allowed to sit in exam if his/her attendance is less than 75%.
a. Take following input from user
i. Number of classes held
ii. Number of classes attended.
b. Print percentage of class attended
c. Print Is student is allowed to sit in exam or not.
"""
class_held=int(input("Enter the number of class held:"))
class_attend=int(input("Enter the number of class attended:"))

percentage_class_attend=(class_attend/class_held)*100

print("Percentage of class attended:",percentage_class_attend)

if percentage_class_attend>=75:
    print("Student is allow to sit in the exam")
else:
    print("Student is not allow to sit in the exam")


#35 
"""
Take Salary as input from User and Update the salary of an employee.
salary less than 10,000, 5 % increment
salary between 10,000 and 20, 000, 10 % increment
salary between 20,000 and 50,000, 15 % increment
salary more than 50,000, 20 % increment
"""
salary=int(input("Enter the Salary of employee:"))

if salary<10000:
    salary=salary+(5/100)*salary
    print("Salary increment 5%\ i.e:",salary)

elif 10000<=salary<=20000:
    salary=salary+(10/100)*salary
    print("Salary increment 10%\ i.e:",salary)

elif 20000<=salary<=50000:
    salary=salary+(15/100)*salary
    print("Salary increment 15%\ i.e:",salary)

elif salary>50000:
    salary=salary+(20/100)*salary
    print("Salary increment 20%\ i.e:",salary)

else:
    print("Salary will not incrementing")
    print("Salary is :",salary)
    

#36 Take three numbers as input from User and print which one is greater or are they equal.
num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))

if num1>num2 and num1>num3:
    print("n1 is the greater ")
elif num2>num1 and num2>num3:
    print("n2 is the greater ")
elif num3>num1 and num3>num2:
    print("n3 is the greater ")
else:
    if num1==num2:
        print("num1 and num2 is equal")
    elif num1==num3:
        print("num1 and num3 is equal")
    elif num2==num3:
        print("num2 and num3 is equal")
    else:
        print(" All are equal")


#37 
"""
An extra day is added to the calendar almost every four years as February 29, and the day is called a leap day. A leap year contains a leap day.
These are the conditions used to identify leap years:
This means the years 2000 and 2400 are leap years, while 1800, 1900, 2100, 2200, 2300 and 2500 are NOT leap years.
Ask a year input from user. And tell if the year entered by user is leap or not.
if the year can be evenly divided by 4, it is then a leap year
but if the year is evenly divided by 4 and also by 100, then it is NOT a leap year
but if the year is evenly divided by 4 and also by 400, then it is a leap
"""
year=int(input("Enter the year :"))

if year%4==0 and year%100==0:
    print("This year is not leap year")
elif year%4==0 and year%400==0:
    print(year,"is leap year")
elif year%4==0:
    print(year,"is leap year")
else:
    print("Invalid year")

