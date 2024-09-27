n=int(input("Enter n : "))

sum=0
for i in range(1,n+1):
    sum = sum + i**2

print("Sum of sq of nos. from 1 to",n,"= ",sum)