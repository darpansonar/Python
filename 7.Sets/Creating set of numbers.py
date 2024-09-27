str=input("Enter numeric elements seperated by a space : ")

A=set(int(x) for x in str.split())

print("Set = ",A)