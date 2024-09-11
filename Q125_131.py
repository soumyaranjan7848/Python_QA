# 125 Write a python program to reverse a list using slicing.
my_list=[2,34,5,66,69,63,34,12,34,200,55]
r=my_list[ : :-1]
print(r)

# 126 Write a python program to get every third element from a list using slicing.
a=[1,2,3,4,5,6,7,8,9,10]
T_E=a[2::3]
print(T_E)

# 127 Implement a python program to split a list into two equal parts using slicing. 
# One list should contain 1st half and another list should contain 2nd half.
b=[2,3,4,5,6,7,8,9]
d=b[:len(b)//2]
e=b[len(b)//2:]
print(d)
print(e)

# 128 Implement a python program to get the last 'n' elements from a list using slicing.
n=int(input("Enter a number:"))
a=[12,23,43,45,67,78,89]
r=a[-n::]
print(r)

# 129 Ask ‘n’ from user. Create a list of lastnelements but in reverse order using slicing.
n=int(input("Enter a number:"))
a=[25,45,47,87,98,36,65,85]
r=a[-1:-n-1:-1]
print(r)

# 130 Ask start and n end index from the user. Create a list from start index to end index using slicing.
start_index=int(input("Enter starting index:"))
end_index=int(input("Enter end index:"))
a=[23,4,34,23,42,77,24,23,4,34,3,99]
r=a[start_index:end_index]
print(r)

# 131 Ask ‘n’ from user. Create a list of first n elements but in reverse order using slicing.
n=int(input("Enter a number:"))
a=[20,12,34,45,6,78,90,23,34,99]
#r=a[-n-1: :-1]
r=a[:n][::-1]
print(r)














