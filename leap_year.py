print("Welcome to the leap year checker!")

done = False

while not done:
    print()
    print("Press ^C to quit.")
    year = int(input("Enter year: "))

    if year % 400 == 0:
        print("true")
    else:
        if year % 100 == 0:
            print("false")
        else: 
            if year % 4 == 0:
                print("true")
            else:
                print("false")
