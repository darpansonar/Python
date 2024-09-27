states={}

for i in range(3):
    st=input("Enter state name : ")
    cap=input("Enter capital of state : ")
    states.update({st:cap})
print("Dict. of states = ",states)

print("\nDisplaying name of states : ")
for i in states:
    print(i,end=" , ")
#or
# states.keys()

print("\nDisplaying name of capitals of states : ")
for i in states:
    print(states[i],end=" , ")
#or
# states.values()

print("\nDisplaying both : ")
for i in states:
    print(i," : ",states[i])