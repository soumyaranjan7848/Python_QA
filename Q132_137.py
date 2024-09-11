# 132 Ask a string from user. Count how many alphabets are there in that string.
my_string=str(input("Enter a string:"))
count=0
for i in my_string:
    if i.isalpha():
        count+=1
print("Number of alphabets in the given string is",count)
    
# 133 Ask a string from user. Count the number of uppercase and lowercase characters in that String.
my_string=str(input("Enter a string:"))
upper,lower=0,0
for char in my_string:
    if char.isupper():  
        upper+=1
    elif char.islower():    
        lower+=1     
print("Upper case letters = ",upper,"\n Lower case letters = ",lower)

# 134 Ask a string from user. Convert all the alphabets to uppercase
my_string=input("Enter a string:")
result=my_string.upper()
print("String after converting to Upper Case = ",result)    

# 135 Ask a string from user. Convert all the alphabets to lowercase.
my_string=input("Enter a string:")
result=my_string.lower()
print("String after converting to Lower Case = ",result)      

# 136 Ask a string from user. Convert uppercase to lowercase and convert lowercase to uppercase and 
# don’t change the other letters.
my_string=input("Enter a string:")
result=""
for char in my_string:
    if char.isupper():
        result += char.lower()
    elif char.islower():
        result += char.upper()
print("Resultant String = ",result)

# 137 Count the number of spaces in a string entered by user.
my_string=input("Enter a string: ")
space_count=my_string.count(' ')
print("The number of space in the given string is : ",space_count)

# 138 Ask a string from user. Print the count of how many alphabets, digits, 
# spaces and symbols (everything else) are there in that string.m
my_string=input("Enter a string: ")
alpha=digit=sym=" "
spa=0
for i in my_string:
    if i.isalpha():
        alpha+=(i)
    elif i.isdigit():
        digit+=(i)
    elif i==' ':
        spa+=1
    else:
        sym+=(i)
print("Alphabets = ",alpha  ,"\nDigits = ",digit,"\nSpaces = ",spa,"\nSymbols = ",sym)




































