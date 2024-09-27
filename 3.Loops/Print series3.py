# if x=3 ---> series = 1/x + 2/x + 3/x

x=int(input("Enter x : "))

sum=0
for i  in range(1,x+1):
    sum = sum + (i/x)

print("Sum of given series : ",sum)

