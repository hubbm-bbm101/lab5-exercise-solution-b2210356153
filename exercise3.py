import random
n = random.randint(0,10)
a = int(input("What is your guess: "))



def asking():
    global a
    a = int(input("What is your guess: "))
    return checking()

def checking():
    if a == n:
            print("Your guess is correct")
            
    else:
        if a > n:
                print ("Decrease your number of guesses")
        else:
                print ("Increase your number of guesses")
    
        

    if a != n:
        return asking()


checking() 