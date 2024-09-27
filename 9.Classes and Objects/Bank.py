bank=str
name=str
acno=int
bal=int
class Bank:
    def __init__(self):
        print("Enter account Information")
        self.bank=input("Enter Bank name : ")
        self.name=input("Enter name : ")
        self.acno=int(input("Enter account no. : "))
        self.bal=int(input("Enter balance : "))

    def display(self):
        print("Bank name   :",self.bank)
        print("Name        :",self.name)
        print("Account no. :",self.acno)
        print("Balance     :",self.bal)

    def deposit(self):
        self.dep=int(input("Enter amount to deposit : "))
        self.bal=self.bal+self.dep

    def withdraw(self):
        self.wit=int(input("Enter amount to withdraw : "))
        self.bal=self.bal-self.wit

    def submenu(self):
        c=int
        while(c!=4):
            c=int(input("\nEnter  1)Deposit  2)Withdraw  3)Display  4)Exit : "))

            if(c==1):
                self.deposit()

            elif(c==2):
                self.withdraw()

            elif(c==3):
                self.display()

            elif(c==4):
                break;

            else:
                print("Wrong input")

print("Customer 1")
b1=Bank()
b1.submenu()

print("\n")

print("Customer 2")
b1=Bank()
b1.submenu()