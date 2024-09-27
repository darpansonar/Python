"""1  2  3  4  5  6  7  8  9  10
2  4  6  8 10 12 14 16 18  20
3  6  9 12 15 18 21 24 27  30
...
10 20 30 40 50 60 70 80 90 100"""

n=int(input("Enter n : "))

for i in range(1,n+1):
    for j in range(1,11):
        print(i*j,end=" ")

    print("")