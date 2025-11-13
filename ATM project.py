balance = 1500

while True:
    print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", balance)
    elif choice == 2:
        deposit = float(input("Enter amount to deposit: "))   
        balance += deposit
        print("Deposit successfully!") 
    elif choice == 3:
        withdraw = float(input("Enter amount to withdraw: "))
        if withdraw <= balance:
            balance -= withdraw
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")   
    elif choice == 4:
        print("Thank You For Using Our ATM.")  
        break
    else:
        print("Invalid option.")       

