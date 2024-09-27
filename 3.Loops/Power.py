a=int(input("Enter base : "))
b=int(input("Enter power : "))

f=1
for i in range(1,b+1,1):
    f=f*a

print(a,"^",b,"=",f)