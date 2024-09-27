list=["mon","tue","wed","thurs","fri","sat","sun"]

for i in list:
    if(i=="wed"): #skipping wed
        continue

    if(i=="sat"): #stopping loop at fri
        break

    print(i)