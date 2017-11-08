from num2words import num2words
prime = 0
composite = 0
negative = 0

user_var = raw_input("insert a number to find if its prime: ")

while not (user_var.lstrip("-").isdigit()):
    user_var = raw_input("insert a number: ")

x = int(user_var)

while x == int(user_var):
    if x > 1:
        for i in range(2, x):
            if(x % i) == 0:
                composite = x
                x = x * 0
                break
        else:
            prime = x
            x = x * 0 + 2
            break
    else:
        if (x == 1):
            x = x * 0 + 3
            break
        elif (x == 0):
            x = x * 0 + 4
            break
        else:
            negative = x
            x = x * 0 + 1
            break

if (x == 0):
    print num2words(composite), "is a composite"
elif (x == 1):
    print num2words(negative), "is a negative, neither prime nor composite"
elif (x == 2):
    print num2words(prime), "is a prime"
elif (x == 3):
    print "one is a zero-divisor"
elif (x == 4):
    print "zero is a zero-divisor"
