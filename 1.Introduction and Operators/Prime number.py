n=int(input("Enter no. : "))

if(n==1):
    print("No. is not prime")

if(n>1):
    for i in range(2,n):
        if(n % i == 0):
            print("No. is not prime")
            break
    else:
        print("No. is prime")




