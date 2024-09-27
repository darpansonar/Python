#Armstrong no. ----> Sum of cube of digits = no. itself

n=int(input("Enter no. : "))

temp=n
sum = 0
while n>0:
    sum = sum + (n % 10)**3
    n = n // 10

# we stored value of n in temp becoz value of n is changing in the loop

if(sum==temp):
    print("It is an armstrong no.")

else:
    print("It is not an armstrong no.")