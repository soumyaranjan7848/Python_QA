# 121 Generate a list of squares of numbers from 1 to 10 using list comprehension.
my_list= [i**2 for i in range(1, 11)]
print(my_list)

# 122 Given a list of strings, create a new list containing the lengths of each string using list comprehension.
my_list=["apple", "banana", "cherry"]
new_list=list(map(len,my_list))
print(new_list)

# 123 Generate a list of strings where each string repeats itself three times,using list comprehension.
my_list=['a','b','c']
new_list=[''.join([i]*3) for i in my_list]
print(new_list)

# 124 Generate a list of list using list comprehension where format should be [[1, ”ODD”], [2, “EVEN”], [3, ”ODD”]].
my_list=[list(i) for i in enumerate (["ODD","EVEN"])]
for i in range(len(my_list)):
    if i%2==0:
        my_list[i][0]=i+1
print(my_list)
























