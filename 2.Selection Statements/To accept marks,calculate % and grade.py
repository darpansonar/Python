print("Enter marks obtained in 3 subjects out of 100 : ")

n1=int(input("Subject 1 : "))
n2=int(input("Subject 2 : "))
n3=int(input("Subject 3 : "))

total = n1 + n2 + n3
per = total*100 / 300

print("Total          :",total)
print("Percentage     :",per)
print("Grade obtained : ")

if(n1>=40 and n2>=40 and n3>=40):
    if(per>=70):
        print("Distinction")
    elif(per>=60 and per<70):
        print("First Class")
    elif(per>=50 and per<60):
        print("Second Class")
    elif(per>=40 and per<50):
        print("Pass")
else:
    print("Fail")


