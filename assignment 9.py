# RAILWAY TICKET BOOKING SYSTEM!

print("WELCOME TO CODERAIL TICKET BOOKING SYSTEM!")
t=int(input("How many tickets you want to book!"))
for i in range(t):
    print(f"-------ticket no. {i+1}-----------")
    name=input("Enter your name: ")
    age=int(input("enter your age: "))
    clas=int(input("enter the class in which you want to travel.(choose 1,2 or 3)\n 1.First Class - ₹1500.\n 2. second class-₹1000.\n 3. third class-₹500 : \n"))
    m=int(input("Do you want to add meal(type 1 for yes,2 for no) : "))
    if clas==1:
        price=1500
        clas_name="first class"
    elif clas==2:
        price=1000
        clas_name="second class"
    else:
        price=500
        clas_name="third class"
    if age<5:
        price=0
    elif age>60:
        price=price+price*20/100
    else:
        pass
    if m==1:
        price=price+200
    else:
        pass
    print("--------------TICKET SUMMARY!-------------")
    print(f"passenger details: \n1. NAME:{name} \n AGE:{age} \n TRAVEL CLASS:{clas_name} \n TOTAL PRICE:{price} ")
print("Enjoy your journey! 🎉")
    
#*******************************************************************************************************************************

#Question 2

#BURGER KING

print("Welcome to Burger King 🍔!")
print("MENU: \n 1. Whopper Burger - ₹150 \n 2. Crispy Veg - ₹100 \n 3. Chicken Wings - ₹120 ")
a=int(input("Enter the item number (1/2/3): "))  
t=int(input("HOW MANY BURGERS YOU WANT TO ORDER: "))
if a==1:
    price=150
    item="Whooper burger"
elif a==2:
    price=100
    item="Crispy veg"
else:
    price=120
    item="Chicken wings"
total=price*t
n=total
code=input("Do you have a coupon code? (yes/no): ").lower()
if code=="yes":
    c=input("Enter your coupon code: ").upper()
    print("Applying coupon...")
    if c=="KING50":
        disc=total*0.5
        total=total-disc
    elif c=="BK20":
        disc=20
        total=total-20
    else:
        print("Invalid coupon code!")
        disc=0
else:
    disc=0
print("\n final bill------------")
print("ITEM: ",item)
print("Quantity: ",t)
print("Original price: ₹",n)
print("Discount applied:  ₹",disc)
print("Final price:  ₹",total)
print("Thanks for ordering at Burger King! 🍟")


    
        
    
    
    

    


    




    
    
    
   