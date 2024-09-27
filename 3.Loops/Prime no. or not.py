n=int(input("Enter no. : "))

flag=0

for i in range(2,n,1):
    if(n%i==0):
        flag=1
        break

if(flag==0):
    print("It is a prime no.")

elif(flag==1):
    print("It is not a prime no.")