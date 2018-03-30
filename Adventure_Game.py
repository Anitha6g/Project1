import random
import time

print("Welcome to the game of Hercules")
print("Only the bold and courageous one wins!!!")
time.sleep(2)
enter = str(input("You see a dark and dusty cave in the middle of the forest,do you wish to enter?(y/n)"))
#enters the cave
if enter in ['y', 'Y', 'Yes', 'yes']:
    print("You have entered the cave and it smells like rotten eggs,deadbodies \
          and the sound of creaks which runs a chill down your spine")
    time.sleep(1)
    print("Your eyes get adjusted to the dark and you then see an an object lying on the ground")
    time.sleep(1)
    print("oh wait its fire breather")
    Fb = str(input("Do you wish to carry it along with you?(y/n)"))
    #picks up fire breather
    if Fb in ['y', 'Y', 'Yes', 'yes']:
        print("Cool!! you now have a fire weapon")
        time.sleep(2)
        Door1 = str(input("You are slowly moving into the cave, you find a door,Do you wish to enter??(y/n)"))
        #Opens door1
        if Door1 in ['y', 'Y', 'Yes', 'yes']:
            print("The door slowly creaks open")
            time.sleep(1)
            print("You enter the room and find something moving!!!!")
            time.sleep(2)
            print("ITS A GIANT 6 HEADED SNAKE!!!!!OH NOOO!!")
            time.sleep(1)
            print("WHAT CAN YOU DOO???")
            time.sleep(2)
            print("Oh wait you have a FIRE BREATHER, use it to destroy the snake")
            fight1 = input("ARE YOU SCARED TO FIGHT THE SNAKE??(y/n)")
            #fights the snake
            if fight1 in ['n', 'N', 'No', 'no']:
                print("The intensity of the fire should be greater than 5 to kill the snake")
                inten = random.randint(4,10)
                if inten > 5:
                    time.sleep(1)
                    print("You are strong, the intesity was"+str(inten)+", you killed that snake within one blow")
                    time.sleep(2)
                    print("As you move deeper into the room, you see something shiny")
                    time.sleep(2)
                    print("Whooho its s heap of gold coins, you're rich")
                    print("The end!!")
                elif inten < 5:
                    time.sleep(1)
                    print("oops the intesity was"+str(inten)+",the snake melts you with the venomic acid it spits out of its mouth")
            #Does not fight the snake
            else:
                print("You are too scared to fight the snake, you try to run!!")
                print("But the door you came through is closed, you have no where to run!")
                time.sleep(2)
                print("OOPS too late!!!, snake has a full stomach now!!")
        #doesnt open the door
        else:
           print("Hmmm!!! you spend time eating your candy bars outside the door, suddenly you are stuck, something wont let you go!!!") 
           time.sleep(2)
           print("DA DA DA, THE END!!")
    #doesnt pick up fire breather
    else:
        print("You choose to fight the monsters with candy bars that you have, unfortunately that doesnt end well for you")
        print("The end!!")
#Doesnt enter the cave
else:
    time.sleep(2)
    print("You go back home without any adventure, make a bowl of maggi, eat and sleep!!")
    