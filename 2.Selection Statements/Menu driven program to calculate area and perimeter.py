print("""Enter 1. To calculate area & perimeter of Square
Enter 2. To calculate area & perimeter of Circle
Enter 3. To calculate area & perimeter of Rectangle
Enter 4. To exit""")
n=int
while(n!=4):
    n = int(input("\nChoice : "))
    if(n==1):
        a=int(input("  Enter side of square : "))
        print("  Area                 :",a**2)
        print("  Perimeter            :",4*a)
    elif(n==2):
        r=int(input("  Enter radius of circle : "))
        print("  Area                   :",3.14*r*r)
        print("  Circumference          :",2*3.14*r)
    elif(n==3):
        l=int(input("  Enter length of rectangle : "))
        w=int(input("  Enter width of rectangle  : "))
        print("  Area                      :",l*w)
        print("  Perimeter                 :",2*(l+w))
    elif(n<1 or n>4):
        print("  Invalid input")
    else:
        exit()

