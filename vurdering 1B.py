import random as random


def game():
    found = False
    sluttall = random.randint(1, 100) #lager et tilfeldig tall mellom 1 og 100
    #print(sluttall)


    while not found:


        tall = int(input("Skriv inn et tall: "))
        if (tall == sluttall):
            found = True
            print("Du fant tallet")
        else:
            if (sluttall > tall):
                print("Tallet er for lavt \n" )
            else:
                print("Tallet er for høyt\n")

game()

