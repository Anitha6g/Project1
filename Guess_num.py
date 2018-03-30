import numpy as np
num_gen = np.random.randint(1,10)
def Guess_num():
    while True:
        num_inp=int(input("Enter the number you guessed:"))
        if type(num_inp) is int:
            if num_inp == num_gen:
                print("you are a Genius!!")
                return False
            elif num_inp > num_gen:
                print("Guessed number is greater than generated number")
            elif num_inp < num_gen:
                print("Guessed number is lower than the generated number")
        else:
            print("Enter a valid integer")
Guess_num()