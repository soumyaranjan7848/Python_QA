# 138 Write a program to reverse the order of words.
#my_string="Hello World"
my_string="Python is good"
word=my_string.split()
result=word[::-1]
rev=" ".join(result)
print(rev)

# 139 Write a program that accepts a string and capitalizes the fi rst letter of each word 
# while converting all other letters to lowercase.
#my_string="hello world"
my_string="Python is good"
#capitalized = my_string.title()
#print(capitalized)
words=my_string.split()
new_words=" ".join(i.title() for i in words)
print(new_words)

# 140 Write a program that reverses each word in a sentence while maintaining the word order. For example,
# "Hello World" should become "olleH dlroW".
my_string1="Hello world"
words=my_string1.split()
reversed_words=[i[::-1] for i in words]
new_words=" ".join(reversed_words)
print(new_words)

# 141 Write a program that converts a string in camelCase to snake_case. For example, converting
# "helloWorldHowAreYou" should result in "hello_world_how_are_you".
my_string=str(input("Enter the string:"))
class_name=my_string
snake_case=""
for char in class_name:
    if char.isupper():
        snake_case+="_"
    snake_case+=char.lower()
print(snake_case)
























