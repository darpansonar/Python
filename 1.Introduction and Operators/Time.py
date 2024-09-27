# To find time in hrs , minutes & seconds

time=int(input("Enter time in seconds : "))

hrs = time//3600
time = time%3600

mins = time//60
time = time%60

print("Hours   : ",hrs)
print("Minutes : ",mins)
print("Seconds : ",time)

