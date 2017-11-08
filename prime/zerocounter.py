var = raw_input("Enter an integer: ")

while not (var.lstrip("-").isdigit()):
    print "Thats not one integer."
    var = raw_input("Please enter an interger: ")

x = int(var)
z = 0
print "You entered: ", var

while x != 0:
    if x == 0:
        z = 0
    else:
        if x > 0:
            x = x - 1
            print x
            z = z + 1
        else:
            x = x + 1
            print x
            z = z + 1

if x == 0:
    if z == 1 or z == -1:
        print "Your input is one number from zero."
    elif int(var) == 0:
        print "Your input is zero!"
    else:
        print "Your input is", z, "numbers from zero."
