# 166 Write a function that accepts an integer and prints the multiplication table for that number up to 10.
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

multiplication_table(5)

# 167 Write a function that accepts an integer and prints whether it is odd or even.
def odd_or_even(n):
    if n%2==0:
        print(f"{n} is even")

    else:
        print(f"{n} is odd")

odd_or_even(5)

# 168 Write a function that takes three numbers as parameters and prints the largest among them.
def largest_num(n1,n2,n3):
    if n1>n2 and n1>n3:
        print(f"largest number is {n1}")
    elif n2>n1 and n2>n3:
        print(f"largest number is {n2}")
    elif n3>n1 and n3>n2:
        print(f"largest number is {n3}")
    else:
        print(f"Invalid number")

largest_num(3,9,4)

# 169 Write a function that takes an integer and prints whether it is a prime number.
def prime_number(n):
    factor=0
    for i in range (1,n+1):
        if n%i==0:
            factor +=1
    if factor==2:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")

prime_number(20)

# 170 Write a function that takes a list of numbers and prints the sum and average of these numbers.
def sum_avg(lst):
    total=sum(lst)
    print(f"sum of all number in list is {total}")
    avg=total/len(lst)
    print(f"average of all the number in the list {avg}")

sum_avg([23,4,5,3,22,3,4,6])

#*********************************OR**OR****OR***OR*********************************

def sum_avg_list(mylist):
    total=0
    for num in mylist:
        total=total+num
    print(f"sum of all number in list is {total}")
    avg=total/len(mylist)
    print(f"average of all the number in the list {avg}")

sum_avg_list([23,4,5,3,22,3,4,6])


# 171 Write a function that accepts a string and prints the frequency of each character in the string.
def frequency(my_string):
    my_dict=dict()
    for ch in my_string:
        if ch not in my_dict:
            my_dict[ch]=1
        else:
            my_dict[ch] +=1

    print(f"{my_dict}")

    for i,j in my_dict.items():
        print(f"{i} occurs {j} times")

frequency('helloooggefe fefs d ')

# 172 Write a function that takes a string and prints whether it is a palindrome.

def check_palindrome(string):
    if string == string[::-1]:
        print(f"This is palindrome :{string}")
    else:
        print(f"This is not palindrome :{string}")

check_palindrome('dsdsadasdsd')



