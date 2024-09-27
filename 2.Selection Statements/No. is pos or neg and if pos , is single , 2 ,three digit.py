n=int(input("Enter a no. : "))

if(n<0):
    print("No. is negative")

if(n==0):
    print("No. is zero")

if(n>0):
    print("No is positive ")
    if(n//10 == 0):
        print("It is single digit no.")
    elif(n//100 == 0):
        print("It is 2 digit no.")
    elif(n//1000 == 0):
        print("It is 3 digit no.")
    else:
        print("It is 4 digit or higher digit no.")