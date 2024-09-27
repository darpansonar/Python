#Perfect no.---> Reverse of a no. = No.  itself eg 121

n=int(input("Enter number : "))

temp=n
rev=0
while(n>0):
    rev = rev*10 + n%10
    n = n//10

print("Number =",temp)
print("Reverse =",rev)

if(temp==rev):
    print(temp,"is a perfect no.")

else:
    print(temp, "is not a perfect no.")

