import random

rolls_value=[]
rolls=5
for i in range(rolls):
    dice = random.randint(1,6)
    rolls_value.append(dice)
print("Dice:")
print("  Attacker: " + str(rolls_value[0]) + "-" + str(rolls_value[1]) + "-" + str(rolls_value[2]))
print("  Defender: " + str(rolls_value[3]) + "-" + str(rolls_value[4]))
