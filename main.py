aliens = 2
password = "ALIENS"
print("Quickly! Aliens are invading  the planet.")
print("You need to actiate the global platforms.")
print("Hope you know the password, for Earth's sake.")
print()
print("---------------------------------------------------------")
print ("       Welcome to the global defence network             ")
print ("---------------------------------------------------------")
print ()
guess = input("Please enter the password: ").upper()
while guess != password:
    print ()
    print ("Incorrect password.")
    print ()
    aliens = aliens ** 2
    print("There are",aliens,"aliens now on Earth. Try again!")
    if aliens > 7400000000:
        break
    print ()
    print ("Password hint: the things that are attacking us.")
    print ()
    guess = input("Please enter the password: "). upper()
    if aliens>7400000000:
        print("Noooooooooo! the aliens out numbered us! All is lost!")
    else:
        print ("Hooray! We won; the world is saved!")
