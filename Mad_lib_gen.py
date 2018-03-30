import random
print("Yay!! Fun with mad lib generators")

Random_name = input("Random name:")
Your_name = input("Your name:")
Random_place = input("Random place:")
Verb = input("Verb:")
Adjective = input("Adjective:")

my_adj = ["stupid","weirdo","kiddish","mental","crazy","jovial"]

print(random.choice(my_adj)+' '+Random_name+' is '+Verb+' to '+Adjective+' '+Your_name+' in '+Random_place)

