aliens = 2
password = "ALIENS"
print("Qickly! aliens are invading  the planet.")
print("you need to actiate the global platforms")
print("Hope you now the passward,for earth's sake")
print()
print("---------------------------------------------------------")
print ("       Welcome to the global defence network             ")
print ("---------------------------------------------------------")
print ()
guess = input(" Please enter the password:").upper()
while guess != password:
    print ()
    print ("Increct password")
    print ()
    aliens = aliens ** 2
    print("There",aliens,"aliens now on Earth. try again!")
    if aliens > 7400000000:
        break
    print ()
    print ("password hint: the things that are attaching us ")
    print ()
    guess = input(" Please enter the password:"). upper()
    if aliens>7400000000:
        print("noooooooooo! the allons out nummberd us all is loost")
    else:
        print ("hooray! we won the would is saved")
