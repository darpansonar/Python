def volume(l=10,b=5,h=5):

    vol = l*b*h
    return vol

print("Volume : ",volume())
print("Volume : ",volume(5)) #l=5,b=10,h=10
print("Volume : ",volume( 5,10))  #h=5
print("Volume : ",volume(5,7,9))