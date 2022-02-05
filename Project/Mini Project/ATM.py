
balance = 100000

option = int(input("Choose option\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Exit\n Enter your choice in number : "))

if option == 1:
    deposit = int(input("How much money do you want to deposit : "))
    result = balance + deposit
    print(f"Your current balance : {result}")

elif option == 2:
    print("Current balance :", balance)
    withdraw = int(input("How much money do you want to withdraw : "))
    result = balance - withdraw
    if result >= 100:
        print(f"Withdrawal amount : {withdraw}\nCurrent balance : {result}")
    else:
        print("Insufficient balance!\nBalance must left at least 100$!")

elif option == 3:
    print("Current Balance :", balance)

elif option == 4:
    print("Thanks for using KPP's bank.\nHave a nice day.")

else:
    print("Option not Available!")
