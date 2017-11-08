print "Tell me a a dice to roll e.g. 4, 6, 20."
print "and i'll roll it for you."
print "write 'quit' to exit."

while (1==1):
    dice = raw_input("Enter: ")

    if dice == "quit":
        break

    while not (dice.isdigit()):
        print "Thats not a dice"
        print "An input for a four sided dice would be 4d or 4."
        dice = raw_input("Please enter a dice: ")
        if dice == "quit":
            break

    if dice == "quit":
        break

    print " "
    x = int(dice)

    from random import randint
    print "I rolled:                ", randint(1, x)

    print " "
