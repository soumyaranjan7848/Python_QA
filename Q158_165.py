#158  Given two lists a, b. Check if two lists have at least one element common in them.
a=[3,4,5,6,7]
b=[9,2,1,3,7]

c=set(a)
d=set(b)
r=c.intersection(d)
print(r)

#159 Python program to fi nd common elements in three lists using sets.
a=[3,4,5,6,7]
b=[9,2,1,3,7]
c=[12,34,23,13,7]

p=set(a)
q=set(b)
r=set(c)

x=p.intersection(q)
result=x.intersection(r)
print(result)

#160 Create 3 sets of your own, find the union of three sets.
set1={2,4,3,5,6,8}
set2={1,2,4,3,5,6}
set3={2,4,1,6,8,9}

a=set1.union(set2)
b=a.union(set3)
print(b)

#161 Write a Python program to remove all elements from a given set.
set1={2,4,3,5,6,8}
set1.clear()
print(set1)

#162 Write a Python program to find the length of a set.
set1={2,4,3,5,6,8,1,32,42,23}
r=len(set1)
print(r)

# 163 Write a Python program to check if two given sets have no elements in common.
set1={2,4,3,5,6,8}
set2={1,22,44,32,52,62}

result=set1.intersection(set2)
if len(result)==0:
    print("Two sets have no elements in common")
else:
    print("Two sets have something common")

# 164 Write a Python program to find elements in a given set that are not in another set.
set1={2,4,3,5,6,8}
set2={1,2,4,3,5,6}
result=set1-set2
print(result)

# 165  Ask a string from user, remove all the duplicates from that string and print that string again
#      (order does’nt matter)

s=str(input("Enter a string :"))
s=set(s)
s=str(s)    
print(s)































































