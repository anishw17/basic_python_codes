# Code By Anish Walke . . . !
import time
import pandas as pd
roll_no =[]
name = []
age = []
gender = []
while True:
    print("1.Enter 1 to add to the list.\n2.Enter 2 to view list.")
    try:
        ui = int(input("Enter your choice :"))
    except ValueError:
        print("Invalid Input, Please try again..!")
    else:
        if ui ==1:
            try:
                n = str(input("Enter the name ;"))
            except ValueError:
                print("Invalid Input, Please try again..!")
            else:
                name.append(n)
            try:
                rn = int(input("Enter the Roll No :"))
            except ValueError:
                print("Invalid Input, Please try again..!")
            else:
                roll_no.append(rn)
            try:
                ag = int(input("Enter the age :"))
            except ValueError:
                print("Invalid Input, Please try again..!")
            else:
                age.append(ag)
            try:
                g = str(input("Enter gender,M for male or F for female :"))
            except ValueError:
                print("Invalid Input, Please try again..!")
            else:
                gender.append(g)
            print("Data added to list successfully")
            df = pd.DataFrame({'Roll No':roll_no,'Name':name,'Age':age,'Gender':gender})
        elif ui == 2:
            print("Loading the List...")
            time.sleep(1)
            print(df)
        else:
            print("Error")


