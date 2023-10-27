rows=int(input("enter the rows:"))
for i in range(1,rows+1):
    print("#"*i)
# PATTERN TO PRINT RIGHT  ANGLE TRIANGLE
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#  PATTERN TO PRINT SQUARE
n=5
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()
#PATTERN OF LEFT SIDED DOWNWARD TRIANGLE
n=5
for i in range(n):
    for j in range(n-i):
            print("*",end="")
    print()
#INVERTED TRIANGLE
n=5
for i in range(n):
    for j in range(n):
        if (j>=i)  :
            print("*",end=" ")
        else:
            print(" ", end=" ")
    print()