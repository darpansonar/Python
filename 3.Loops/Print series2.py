# find sum of x^1 + x^2 + x^3 + x^4 + x^5

x=int(input("Enter no. : "))

sum=0
for i in range(1,6):
    sum = sum + x**i

print("Sum = ",sum)