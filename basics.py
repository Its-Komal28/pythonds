naam=input("enter name")
for i in range(0,len(naam)):
    print(naam)
#printing star pattern...
for i in range(5):
    for j in range(0,i+1):
        print("*",end="")
    print()
#practicing star questions...
n=5
for i in range(n):
    for j in range(n):
        print("*",end="  ")
    print()
n=5
for i in range(n):
    for j in range(n):
        print("*",end="")
    print(n)
#increasing triangle pattern
n=5
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
#decreasing triangle pattern
n=5
for i in range(n):
    for j in range(n,i,-1):
        print("*",end=" ")
    print()
n=5
for i in range(n):
    for j in range(i,n):
        print("@",end=" ") 
    print() 
#right sided triangle

n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    
    
    for j in range(i+1):
        print("*",end="")
    print()
#right sided triangle
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end='')
    for j in range(i,n):
        print("*",end="")
    print()
#hill pattern
n=5
for i in range(n):
    for j in range(i,n):
        print(" ",end="")
    for j in range(i):
        print("*",end="")
    for j in range(i+1):
        print("*",end="")
    print()
#reverse hill pattern
n=5
for i in range(n):
    for j in range(i+1):
        print(" ",end="")
    for j in range(i,n):
        print("*",end="")
    for j in range(i,n-1):
        print("*",end="")
    print()
#diamond pattern
n=5
for i in range(n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range(n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n):
        print("*",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    print()   
str="komal"
print(type(str)) 
    
  
      

        
        