import random
hang_list = ["Vemana","Christ","Krupa","Saptha"]
hang_rand = random.choice(hang_list)
hang_ele = hang_rand
count=0
print(hang_ele)

#def vali(count):
#    if count >= 3:
#        print("Good job!! You won, the word is "+ str(hang_ele))
#    else:
#        print("Better luck next time")
#        
#for i in range(1,6):
#    inp_let=str(input(("Enter the guessed letter number "+ str(i) +":")))
#    if any(inp_let in s for s in hang_ele):
#        print("Yay the letter is present")
#        count+=1
#    else:
#        print("Letter not found in word,enter again")
#vali(count)  


for i in range(1,6):
    inp_let=str(input(("Enter the guessed letter number "+ str(i) +":")))
    if any(inp_let in s for s in hang_ele):
        print("Yay the letter is present")
        count+=1
    else:
        print("Letter not found in word,enter again")
if count >= 3:
        print("Good job!! You won, the word is "+ str(hang_ele))
else:
        print("Better luck next time")

        
    


