while True :
       name = input("Enter the Name: ")
       age = int(input("Enter the Age: "))
       gender = input("Enter the Gender: ")
       t1 =[name, age, gender] 
       if t1[1] >= 30: 
        if t1[2] == "male":
            print("Thiru",name)    
        else:
            print("Thirumathi",name)
       else:
        if t1[2] == "male":
            print("Selvan",name)
        else: 
            print("Selvi", name)
       choice = input ("Are you wants to Contine?: ") 
       if choice == "yes":   
            continue 
       else: 
            break