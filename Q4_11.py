#4 Write a Python program to add two numbers entered by the user.
num1=int(input("Enter 1st number:"))
num2=int(input("Enter 2nd number:"))

res=num1+num2
print(res)

#5 Convert a string to an integer and vice versa.
a="200"
b="300"

print(type(a))

x=int(a)
print(type(x))

c=str(x)
print(type(c))

#6 Write a Python program to calculate the area of a rectangle using user input for length and width.
length=int(input("Enter the length of rectangle:"))
width=int(input("Enter the width of rectangle:"))

area= length*width

print(area)

#7 Write a Python program to calculate the average of three numbers entered by the user.
n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))
n3=int(input("Enter the 3rd number:"))

avg=(n1+n2+n3)/3
print(avg)
 
#8 Convert a float to an integer and vice versa.
a=20.2
b=3.3

print(type(a))

x=int(a)
print(type(x))

c=float(x)
print(type(c))


#9 Write a program that converts a temperature in Fahrenheit to Celsius.[Celsius = (Fahrenheit - 32) * 5/9]
f=float(input("Enter the fahrenheit: "))
c=(f-32)*5/9
print(f,"Fahrenheit = ",c,"Celsius")

#10 Calculate sum of 5 subjects and Find percentage.
Math=float(input("Enter the Mark of Mathematics:"))
Eng=float(input("Enter the Mark of English:"))
Phy=float(input("Enter the Mark of Physics:"))
Che=float(input("Enter the Mark of Chemestry:"))
Bio=float(input("Enter the Mark of Biology:"))

sum=(Math+Eng+Phy+Che+Bio)
print("Sum of 5 subject is :",sum)
if sum>500:
    print("Invalid Sum")
else:
    Percentage=(sum/500)*100
    print("Total Percentage is :",Percentage)

#11 Ask number of games played in a tournament. Ask the user number of games won and number of games loss. 
# Calculate number of tie and total Points. (1 win= 4 points, 1 tie =2 points)
game_played=int(input("Number of game played:"))
win=int(input("Number of game won:"))
loss=int(input("Number of game loss:"))

game_tie=game_played-win-loss
print("Game tie :",game_tie)

Total_point=(win*4)+(game_tie*2)
print("Total point is :",Total_point)







