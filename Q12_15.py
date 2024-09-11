#12 Write a Python program that takes two numbers as input and performs the following operations: 
#addition, subtraction, multiplication, division, and modulus. Display the results.
n1=float(input("Enter the first Number:"))
n2=float(input("Enter the Second Number:"))

add=n1+n2
print("Addition of two number is :",add)

sub=n1-n2
print("Substraction of two number is:",sub)

mul=n1*n2
print("Multipliction of two number is :",mul)

div=n1/n2
print("Division of two number is :",div)

mod=n1%n2
print("Modulus of the two number is :",mod)


#13 Write a Python program to swap the values of two variables without using a temporary variable.
x=5
y=10
print("Before the Swaping:")
print("x=",x)
print("y=",y)

x,y=y,x
print("After the swaping:")
print("x=",x)
print("y=",y)

#14 Write a Python program to calculate the compound interest for a given principal,
# rate of interest, and time period. Ask everything from the user.
p=float(input("Enter the amount of principal:"))
r=float(input("Enter the amount of intrest:"))
t=float(input("Enter the time period:"))

compound_interest=(p*t*r/100)
print("Compound Intrest is :",compound_interest)

#15 Write a Python program that takes the radius of a circle as input and calculates its area. 
#Use the formula: Area = 3.14 * r^2.
r=float(input("Enter the radius of circle:"))
area=(3.14*(r**2))
print("Area of the circle is :",area)


