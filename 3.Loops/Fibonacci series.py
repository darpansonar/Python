n=int(input("Series till how many places : "))

a=1
b=2
print(a,b,end=" ")

for i in range(1,(n+1)-2,1):   #(n+1)-2 becoz a and b are already considered
    c=a+b
    print(c,end=" ")

    a=b
    b=c