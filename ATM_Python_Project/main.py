from account import Account
from bank import Bank
import menu


class Main:

    def run():
        bank = Bank()
        

        while True:
            
            menu.showmenu()
            choice = int(input("Enter your choice : "))

            match choice:

                case 1:
                    acc_no = input("Please enter your account number : ")
                    pin = input("Your pin number : ")
                    acc = bank.login(acc_no, pin)
                    if acc:
                        print(f"Your balance : RM{acc.checkbalance()}")
                        print("")
                    else:
                        print("Please Create account first")
                        print("-" * 30)

                        print("")

                case 2:
                    acc_no = input("Enter account number: ")
                    pin = input("Enter pin: ")
                    acc = bank.login(acc_no, pin)
                    if acc:
                        amount = float(input("Enter deposit amount: "))
                        if acc.deposit(amount):
                            print("Deposit successful!")
                            print(f"New balance: RM{acc.checkbalance()}")
                            print("-" * 30)

                            print("")
                        else:
                            print("Invalid amount!")
                            print("-" * 30)

                            print("")
                    else:
                        print("Login failed!")
                        print("-" * 30)

                        print("")

                case 3:
                    acc_no = input("Enter you account number : ")
                    pin = input("Your pin : ")
                    acc = bank.login(acc_no, pin)

                    if acc:
                        amount = float(input("Enter withdraw amount : "))
                        if acc.withdraw(amount):
                            print("Withdraw successful")
                            print(f"New balance: RM{acc.checkbalance()}")
                            print("-" * 30)

                            print("")
                        else:
                            print("Invalid amount!")
                            print("-" * 30)

                            print("")

                    else:
                        print("Login failed!")
                        print("-" * 30)

                        print("")

                case 4:
                    acc_no = input("Enter you account number : ")
                    pin = input("Your pin : ")
                    acc = bank.add_account(acc_no, pin, 0)
                    print("Account created successfully!")
                    print(f"Your current balance: RM{acc.checkbalance()}")
                    print("-" * 30)

                    print("")

                case 5:
                    print("Exiting system... Goodbye!")
                    print("-" * 30)

                    print("")
                    break

                case _:
                    print("Invalid option, try again.")
                    print("-" * 30)

                    print("")


Main.run()
