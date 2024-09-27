def largest(a,b,c):
    if (a > b and a > c):
        print(a,"is the largest")
    elif (b > a and b > c):
        print(b, "is the largest")
    elif (c > b and c > a):
        print(c, "is the largest")
    else:
        print("2 or more are equal")

def smallest(a,b,c):
    if (a < b and a < c):
        print(a, "is the smallest")
    elif (b < a and b < c):
        print(b, "is the smallest")
    elif (c < b and c < a):
        print(c, "is the smallest")
    else:
        print("2 or more are equal")


ans=0
while(ans!=3):
    ans=int(input("Enter : 1] Largest  2] Smallest  3] Exit :"))

    if(ans==1):
        a = int(input("Enter num1 : "))
        b = int(input("Enter num2 : "))
        c = int(input("Enter num3 : "))
        largest(a,b,c)

    elif(ans==2):
        a = int(input("Enter num1 : "))
        b = int(input("Enter num2 : "))
        c = int(input("Enter num3 : "))
        smallest(a,b,c)

    elif(ans==3):
        exit()

    else:
        print("Invalid input")