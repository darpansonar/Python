def power(a,b):
    p=1
    for i in range(1,b+1):
        p = p * a
    return p

a=int(input("Enter base : "))
b=int(input("Enter exponent : "))

print(a,"^",b,"=",power(a,b))