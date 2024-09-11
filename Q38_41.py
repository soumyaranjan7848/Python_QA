#38 Write a program that takes three numbers as input and determines the largest one using 
#nested if-else statements. Make sure all 3 numbers entered by user are diff erent.

num1=int(input("Enter the 1st number:"))
num2=int(input("Enter the 2nd number:"))
num3=int(input("Enter the 3rd number:"))


if num1 != num2 and num1 != num3 and num2 != num3:
    if num1 > num2:
        if num1 > num3:
            print("The first number is the largest.")
        else:
            print("The third number is the largest.")
    else:
        if num2 > num3:
            print("The second number is the largest.")
        else:
            print("The third number is the largest.")
else:
        print("Please enter three different numbers.")

#39 Write a program that checks if a given year is a leap year. 
#Leap years are divisible by 4, but not by 100 unless they are also divisible by 400.
        
year=int(input("Enter the year:"))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
        print(f"{year} is not a leap year.")

     
#40 Create a program that calculates the price of a movie ticket based on the age of the customer. 
#If the customer is under 12, the ticket costs $5; if they are between 12 and 65, 
#the ticket costs $10; otherwise, it's $7.

age=int(input("Enter the age of customer:"))

if age<12:
     ticket_price=5
else:
     if age<=65:
          ticket_price=10
     else:
          ticket_price=7
print("Ticket price Rs.",ticket_price,"For the age of",age)

#41 
"""
Write a program that calculates a person's BMI based on their height (in meters) and weight (in kilograms). 
Use the following formula: BMI = weight / (height^2). Then, classify the BMI according to the 
following ranges:
Underweight: BMI less than 18.5
Normal weight: BMI 18.5 - 24.9
Overweight: BMI 25 - 29.9
Obesity: BMI 30 or greater
"""     
height=float(input("Enter the height of person:"))
weight=float(input("Enter the weight of person:"))

BMI=weight/(height**2)

if BMI<18.5:
     print("Underweight")
else:
     if BMI<=24.9:
          print("Normal Weight")
     else:
          if BMI<=29.9:
               print("Overweight")
          else:
               print("Obesity")



















