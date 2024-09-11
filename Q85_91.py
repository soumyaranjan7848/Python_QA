#85 Print the following pattern.
"""
        *
      * *
    * * *
  * * * *
* * * * *
"""
for i in range(1,6):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(1,i+1):
        print("*",end=" ")
    print()

#86 Print the following pattern.
"""
        1
      1 2
    1 2 3
  1 2 3 4
1 2 3 4 5 
"""
for i in range(1,6):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print()

#87 Print the following pattern.
"""
        1
      2 2
    3 3 3
  4 4 4 4
5 5 5 5 5
"""
for i in range(1,6):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(i,end=" ")
    print()

#88 Print the following pattern.
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
for i in range(1,6):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(1,(i*2)): #(i*2)-1 also work
          

# OR
#    for k in range(1,i+1):   
#        print("*",end=" ")
#    for l in range(1,i):
          print("*",end=" ")
    print()

#89 Print the following pattern.
"""
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
  * * * * * * * 
    * * * * *
      * * *
        *
"""
for i in range(1,6):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range(1,(i*2)):
        print("*",end=" ")
    print()
for l in range(4,0,-1):
    for m in range(l,5):
        print(" ",end=" ")
    for n in range((l*2)-1):
        print("*",end=" ")
    print()

#90 Print the following pattern.
"""
* * * * * * * * *
  * * * * * * * 
    * * * * *
      * * *
        *
"""
for l in range(5,0,-1):
    for m in range(l,5):
        print(" ",end=" ")
    for n in range((l*2)-1):
        print("*",end=" ")
    print()

#91 Print the following pattern.
"""
* * * * * * * * *
  * * * * * * * 
    * * * * *
      * * *
        *
      * * *
    * * * * *
  * * * * * * *
* * * * * * * * *
"""
for i in range(5,0,-1):
    for j in range(i,5):
        print(" ",end=" ")
    for k in range((i*2)-1):
        print("*",end=" ")
    print()
for l in range(1,6):
    for m in range(l,5):
        print(" ",end=" ")
    for n in range(1,(l*2)):
        print("*",end=" ")
    print()
















