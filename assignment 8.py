#WEEKLY ASSIGNMENT
# Question 1
for i in range(1,51):
    if i%3==0 and i%5!=0 :
        print("Fizz",end=" ")
    elif i%5==0 and i%3!=0:
        print("Buzz",end=" ")
    elif i%3==0 and i%5==0:
        print("FizzBuzz",end=" ")
    else:
        print(i,end=" ")
        
#**************************************************************************

#Question 2
print("Prime numbers between 1 and 100 are:")
for i in range(2,101):
    for j in range(2,i):
        if i%j==0:
            break
    else:
        print(i,end=" ")
        
#****************************************************************************

#Question 3
marks=int(input("enter your score between 0 and 100:"))
if 90<marks<=100:
    print("You got Grade A")
elif 80<marks<=90:
    print("You got Grade B")
elif 70<marks<=80:
    print("You got Grade C")
elif 60<marks<=70:
    print("You got Grade D")
else:
    print("You got Grade F")
    
#*******************************************************************************

#Question 4
num=int(input("enter the number:"))
print(f"Multiplication table of {num} is:")
for i in range(1,11):
    print(num,"*",i,"=",num*i)
    
#********************************************************************************

#Question 5
lst=[i*i for i in range(1,21) if i%2==0]
print("List of squares of even numbers from 1 to 20 is:",lst)

#*********************************************************************************

#Question 6
year=int(input("enter the year you want to check:"))
if (year%400==0) or (year%4==0 and year%100!=0):
    print("It is a leap year")
else:
    print("It is not a leap year")
    
#**********************************************************************************

#Question 7
a=float(input("Enter the first side of a triange"))
b=float(input("Enter the second side of a triange"))
c=float(input("Enter the third side of a triange"))
if a+b>c and a+c>b and b+c>a:
    if a==b==c:
       print("IT IS AN EQUILATERAL TRIANGLE")
    a=False
    if a**2==b**2+c**2 or b**2==a**2+c**2 or c**2==b**2+a**2:
        a=True
    elif a==b or b==c or c==a:
        if a:
            print("IT IS A RIGHT ANGLED AND AN ISOSCELES TRIANGLE")
        else:
            print("IT IS AN ISOSCELES TRIANGLE")
    elif a:
        print("IT IS A RIGHT ANGLED TRIANGLE")
    else:
        print("IT IS A SCALENE TRIANGLE")
else:
    print("IT IS NOT A VALID TRIANGLE")
    
#***********************************************************************************

#Question 8
num=int(input("Enter an integer:"))
if num>0:
    print("it is a positive integer")
elif num<0:
    print("it is a negative integer")
else:
    print("the integer is zero")
    
#*************************************************************************************

#Question 9
password = input("Enter your password: ")
has_upper = False
has_lower = False
has_digit = False
has_special = False
special_characters = "!@#$%^&*()-_=+[]{}|;:',.<>?/`~"
for char in password:
    if char.isupper():
        has_upper = True
    elif char.islower():
        has_lower = True
    elif char.isdigit():
        has_digit = True
    elif char in special_characters:
        has_special = True
if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
    print("Strong password ")
else:
    print("Weak password ")
    print("Password must:")
    if len(password) < 8:
        print("- Be at least 8 characters long")
    if not has_upper:
        print("- Include at least one uppercase letter")
    if not has_lower:
        print("- Include at least one lowercase letter")
    if not has_digit:
        print("- Include at least one digit")
    if not has_special:
        print("- Include at least one special character (!, @, #, $, etc.)")
        
#****************************************************************************************************

#Question 10
weight=float(input("enter your weight in kilograms"))
height=float(input("enter your height in meters"))
bmi=weight/(height**2)
print("f your bmi is {bmi}")
if bmi< 18.5:
    print("Underweight")
elif 18.5 <= bmi < 24.9:
    print("normal weight")
elif 25 <= bmi < 29.9:
    print("Overweight")
else:
    print("obesity")
    
#*****************************************************************************************************

#Question 11

num=int(input("enter a number from 1 to 7 representing a day of the week"))
if num==1:
    print("its monday")
elif num==2:
    print("its tuesday")
elif num==3:
    print("its wednesday")
elif num==4:
    print("its thursday")
elif num==5:
    print("its friday")
elif num==6:
    print("its saturday")
elif num==7:
    print("its sunday")
else:
    print("invalid input!")
    
#*******************************************************************************************

#Question 12
price=float(input("enter the price of the product:$"))
if price>1000:
    Discount=price*10/100
elif 500<=price<=1000:
    Discount=price*5/100
else:
    Discount=0
total=price-Discount
print("Your discount is",Discount)
print("Your total:",total)

#*********************************************************************************************

#Question 13

sum=0
n=int(input("Enter a number"))
for i in range(n+1):
    sum=sum+i
print(f"Sum of first {n} numbers is: {sum}")

#**********************************************************************************************

#Question 14

employee_details={101:{"name":"Love","department":"Manager","salary":100000},
            102:{"name":"Komal","department":"HR","salary":90000},
            103:{"name":"preeti","department":"web","salary":80000},
            104:{"name":"yasmeen","department":"Manager","salary":40000}}

lst=[employee_details[i]["name"] for i in employee_details if employee_details[i]["salary"]>50000]
print("LIST OF EMMPLOYEES WITH SALARY>50000",lst)

#*********************************************************************************************************

#Question 15

str=input("enter a string: ")
n=0
for i in str:
    if i=="a" or i=="A" or i=="e" or i=="E" or i=="i" or i=="I" or i=="o" or i=="O" or i=="U" or i=="u":
        n=n+1
print("number of vowels in given string:",n)

#***********************************************************************************************************

#Question 16

num=input("enter a  number")
sum=0
for i in num:
    if i.isdigit():
        sum=sum+int(i)
print("sum of digits of the given number is:",sum)

#**************************************************************************************************************

#Question 17
n=int(input("enter an integer:"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
#***************************************************************************************************************

#Question 18
import random
secret_number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 7 attempts to guess it!")
print(secret_number)
for i in range(1,8):
    guess=int(input("Enter your guess:"))
    if guess>secret_number:
        print("Too high")
    elif guess< secret_number:
        print("Too low")
    else:
        print(f"You guessed the right number in {i} attempts")
        break
else:
    print(f"Sorry! You've used all attempts. The number was {secret_number}.")
    
#**********************************************************************************************************

#Question 19
num=int(input("enter a number"))
print("even numbers upto this numbar are:")
for i in range(1,num):
    if i%2==0:
        print(i,end=" ")
        
#************************************************************************************************************

#Question 20

numbers = [12, 25, 7, 30, 25, 42, 55, 25, 64, 18]
#tells number 25 exists or not
if 25 in numbers:
    print("25 exists in the given list.")
else:
    print("element 25 doesnot exists in the given list.")
#Length of given list.
print("Length of the given list is:",len(numbers))
#Total occurence of element 25 in the list,
n=0
for i in numbers:
    if i==25:
        n=n+1
print(f"25 occurs {n} times in the list.")
#Traverse of each element.
print("Traverse of each element:")
for i in numbers:
    print(i,end=" ")
print()
#shows all even numbers.
print("Even numbers in the list:")
for i in numbers:
    if i%2==0:
        print(i,end=" ")
        
#***********************************************************************************************

#Question 21
s=input("Enter a string (minimum 10 words and maximum 19 words))")
if len(s)>=10 and len(s)<=19:
    print("Full string: ",s)  #prints full string.
    a=len(s)
    print("length of this string is:",a)                     #prints length of a string.
    if s==s[::-1]:
        print("it is palindrome")
    else:
        print("not a palindrome.")     #checks if a string is palindrome or not.
    m=a//2                             
    print("middle element is:",s[m])    #prints middle element.
    print("second last element:",s[-2]) #prints second last element.
else:
    print("Enter a valid string!")
    
#*************************************************************************************************

#Question 22

print("Welcome to Calci:")
print("1. Power")
print("2. Sum")
print("3. Sub")
print("4. Multiple")

choice = int(input("\nEnter your choice."))

if choice == 1:
    a = int(input("Enter base number for Power: "))
    b = int(input("Enter exponent number for Power: "))
    print("Result is", a ** b)

elif choice == 2:
    a = int(input("Enter 1st Number for Sum: "))
    b = int(input("Enter 2nd number for Sum: "))
    print("Sum is", a + b)

elif choice == 3:
    a = int(input("Enter 1st Number for Subtraction: "))
    b = int(input("Enter 2nd number for Subtraction: "))
    print("Difference is", a - b)

elif choice == 4:
    a = int(input("Enter 1st Number for Multiplication: "))
    b = int(input("Enter 2nd number for Multiplication: "))
    print("Product is", a * b)

else:
    print("Invalid choice! Please select between 1 to 4.")
    
#***************************************************************************************************

#Question 23

X = ['abc', 'xyz', 'aba', '1221'] 
count = 0
for word in X:
    if len(word) >= 2 and word[0] == word[-1]:
        count += 1
print("Output:")
print(count)   

#**********************************************************************************************************
            



         


