import numpy as np
print("Your roll has the number :" + str(np.random.randint(1,6)))
chance2 = input("Do you want to roll again??:(y/n) : ")
if chance2 == 'y':
    print("Your roll has the number :" + str(np.random.randint(1,6)))
else:
    exit()

