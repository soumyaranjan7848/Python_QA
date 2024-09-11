#66 Print the following pattern
"""
* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
"""
for i in range(1,6):
    for j in range(1,6):
        print("*",end=" ")
    print()

#67 Print the following pattern.
"""
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
1 2 3 4 5
"""
for i in range(1,6):
    for j in range(1,6):
        print(j,end=" ")
    print()

#68 Print the following pattern.
"""
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
5 4 3 2 1
"""
for i in range(1,6):
    for j in range(5,0,-1):
        print(j,end=" ")
    print()

#69 Print the following pattern.
"""
1 1 1 1 1
2 2 2 2 2
3 3 3 3 3
4 4 4 4 4
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(1,6):
        print(i,end=" ")
    print("This is 70")

#70 Print the following pattern. 
"""
5 5 5 5 5
4 4 4 4 4
3 3 3 3 3
2 2 2 2 2
1 1 1 1 1
"""
for i in range(5,0,-1):
    for j in range(5,0,-1):
        print(i,end=" ")
    print()

#71 Print the following pattern. 
n=int(input("Enter n:"))
for i in range(1,n+1):
    for j in range(1,6):
        print(i,end=" ")
    print()

#72 Print the following pattern. 
N=int(input("Enter N:"))
for i in range(N,0,-1):
    for j in range(1,6):
        print(i,end=" ")
    print()









    




