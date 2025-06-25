print("WELCOME!")
print("ENTER YOUR CHOICE! \n 1. a--add \n 2. l--list \n 3. s--search \n 4. v--view \n 5. d--delete \n 6. q--quit")
data=[ { "name": "Forrest Gump", "year": 1994, "duration": 142, "genres": ["Drama", "Romance"] },
    { "name": "Avengers: Endgame", "year": 2019, "duration": 181, "genres": ["Action",
    "Adventure", "Drama"] }, { "name": "Back to the Future", "year": 1985, "duration": 114,
    "genres": ["Adventure", "Comedy", "Sci-Fi"] } ]
while True:
    choice=input("enter your choice(a,l,s,v,d or q): ").lower()
    if choice=="a":
        n=input("Enter movie name: ")
        y=int(input("Enter the year: "))
        d=int(input("Enter its duration in minutes: "))
        li=[]
        ge=int(input("How many generes do you want to add for the movie: " ))
        if ge==0:
            print("Enter atleast one genre")
        else:
            for i in range(ge):
                a=input("Enter genre:")
                li.append(a)
            print("your selected genres: ",li)
        di={"name":n,"year":y,"duration":d,"genres":li}
        data.append(di)
        print("Updated data is:",data)
    elif choice=="l":
        if len(data)==0:
            print("No movies saved")
        else:
            for i in range(len(data)):
                print(i+1,".",data[i]["name"],"--",data[i]["year"])
    
    elif choice=="s":
        search=input("enter the movie you want to search: ").lower()
        for i in range(len(data)):
            if search in data[i]["name"].lower():
                t=0
                print(t+1,")",data[i]["name"],"--",data[i]["year"])
                t+=1    
                break        
            else:
                print("no movies saved")

    elif choice=="v":
        ind=int(input("Enter the index of movie you want to view: "))
        if ind<=len(data):
            print(data[ind-1])
        else:
            print("Invalid index number")
            
    elif choice=="d":
        ind=int(input("Enter the index number if the movie you want to delete: "))
        if len(data)==0:
            print("No movies saved")
        else:
            if ind<=len(data):
                del data[ind]
            else:
                print("Invalid index number")
                
    elif choice=="q":
        print("Goodbye!")
        break
    else:
        print("invalid choice")
            
    
        
            
            

            
            
        
    
    
           
    

