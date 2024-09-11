#73 Print the following pattern.
"""
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(j,end=" ")
    print()

#74 Print the following pattern.
"""
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end=" ")
    print()

#75 Print the following pattern.
"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print("Done")

#76 Print the following pattern.
"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1
"""
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

#77 Print the following pattern.
"""
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""
for i in range(5,0,-1):
    for j in range(5,i-1,-1):
        print(i,end=" ")
    print()

#78 Print the following pattern.
"""
*
* *
* * *
* * * *
* * * * *
"""
for i in range(1,6):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()

#79 Print the following pattern.
"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4
5
"""
for i in range(1,6):
    for j in range(5,i-1,-1):
        print(j,end=" ")
    print()

#80 Print the following pattern.
"""
5 5 5 5 5
4 4 4 4
3 3 3
2 2
1
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(i,end=" ")
    print()

#81 Print the following pattern.
"""
* * * * *
* * * *
* * *
* *
*
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print("*",end=" ")
    print()

#82 Print the following pattern.
"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
for i in range(5,0,-1):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()

#83 Print the following pattern.
"""
1
2 3
4 5 6
7 8 9 10
11 12 13 14 15
"""
n=1
for i in range(1,6):
    for j in range(1,i+1):
        print(n,end=" ")
        n=n+1
    print()

#84 Print the following pattern.
"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""
for i in range(1,6):
    for j in range(i,0,-1):
        print(j,end=" ")
    print()
















