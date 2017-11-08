from num2words import num2words
global y
x, y, z, = 0, 0, 0
list_of_primes = []

var = raw_input("Enter a positive integer to find the primes from it to zero: ")

while not (var.isdigit()):
    print "Thats not one positive integer."
    var = raw_input("Please enter an interger: ")

print "You entered: ", var

def findprime(x):
    if x > 1:
        for i in range(2, x):
            if(x % i) == 0:
                break
        else:
            global y
            y += 1
            list_of_primes.append(x)
    if x == 2:
        1==1

while x != int(var):
    x += 1
    findprime(x)
    z += 1

if x == int(var):
    if z == 1:
        print "Your input is one and has zero primes between it and zero."
    elif int(var) == 0:
        print "Your input is zero!"
    elif int(var) == 2:
        print "Your input is two and has one prime between it and zero."
    else:
        print "The input is", z, "numbers from zero and", y, "primes from it to zero."

print "The primes: ", (list_of_primes)
