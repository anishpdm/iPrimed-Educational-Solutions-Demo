 
# printing the starting line  
print("WELCOME TO A Restaurant")  

sum=0  
# creating options  
while True:  
    print("\nMAIN MENU")  
    print("1. Tea")  
    print("2. Coffee")
    print("3. View Total Bill")  
    print("3. Exit")  
    choice1 = int(input("Enter the Choice:"))  
  
    if choice1 == 1:
        sum=sum+4
     
      
    elif choice1 == 2:  
        sum=sum+5
      
    elif choice1 == 3:  
        print(sum)
    elif choice1 == 4:  
        break   
      
    else:  
        print("Oops! Incorrect Choice.")  