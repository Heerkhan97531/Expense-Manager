# Expense Tacker Project
print("===============Welcome to Expense Manager==================")
expensesList = [] # list of the expences usig dictionary
while True:
    print("========Menu=============")
    print("1.Add expense ")
    print("2.View all expence")
    print("3.Calculate all spending")
    print("Exit")

#1. ADD EXPENCE
    choice = int(input("Enter your choice:"))
    if(choice==1):
        date = input("Enter the date: ")
        category = input("Enter the category of expense: ")
        description = input("Enter the details of expense:")
        amount = float(input("Total amount: "))

        expense = {
            "date": date ,
            "category" : category , 
            "description" : description ,
            "amount" : amount
        }

        expensesList.append(expense)
        print("Expenses added successfully!")
#2. VIEW ALL EXPENCES        
    
    elif (choice ==2):
        if (len(expense)==0):
            print("You don't have to spent money.")
        else:
            count =1
            for eachexpence in expensesList:
                print(f"Expence {count}: {eachexpence["date"]}, {eachexpence["description"]}, \
                {eachexpence["amount"]}")    
                count+=1

#3. VIEW TOTAL SPENDING
    elif (choice == 3):
        total =0
        for eachexpence in expensesList:
            total = total + eachexpence["amount"] 
            print("Total expence is :",total) 

#4. EXIR FROM THE FINANACE APPLICATON
    elif(choice ==4): 
        print("Thank you for coming!. \n " \
        "If you don't want to check your expense you can EXIT from the application.")
        break
    else:
        print("INVALD CHOICE, TRY AGAIN")
    
