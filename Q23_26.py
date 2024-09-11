#23 Write a Python program that takes an integer input and prints whether it's positive, negative. 
#(Consider 0 as positive)
n=int(input("Enter the Number:"))

if n>=0:
    print("The number is positive")

else:
    print("The number is Negative")

#24 Write a program that takes a character as input and prints whether it's a vowel or a consonant. 
#(Multiple OR will be used)
char=input("Enter the character:")

if char=='a' or char=='e' or char=='i' or char=='o' or char=='u':
    print("The character is vowel i.e",char)

else:
    print("The character is consonant i.e",char)


#25 Write a program that takes two numbers as input and checks if the first number is divisible by the second.
n1=int(input("Enter the 1st number:"))
n2=int(input("Enter the 2nd number:"))

if (n1%n2)==0:
    print("YES! first number is divisible by the second")
else:
    print("first number is not divisible by the second")

#26
#A student will not be allowed to sit in exam if his/her attendance is less than 75%.
#Take following input from user
#Number of classes held
#Number of classes attended.
#Print percentage of class attended
#Print Is student is allowed to sit in exam or not.

Class_held=int(input("Number of class held:"))
Class_attend=int(input("Number of class attend:"))

percentage_of_class_attended=(Class_attend/Class_held)*100
print("Print percentage of class attended:",percentage_of_class_attended)

if percentage_of_class_attended<75:
    print("student will not be allowed to sit in exam")
else:
    print("student will be allowed to sit in exam")
















