n=int(input("Enter n :"))

sum_even=0
sum_odd=0

for i in range(1,n+1):
    if(i%2==0):
        sum_even = sum_even + i

    elif(i%2==1):
        sum_odd = sum_odd + i

print("Sum of even nos. from 1 to",n,": ",sum_even)
print("Sum of odd nos. from 1 to",n,": ",sum_odd)

