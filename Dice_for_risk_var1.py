import random

def roll(rolls):
    rolls_value=[]
    for i in range(rolls):
        dice = random.randint(1,6)
        rolls_value.append(dice)
    return rolls_value

a=(roll(3))
d=(roll(2))
print("Dice:")
print("  Attacker: " + str(a[0]) + "-" + str(a[1]) + "-" + str(a[2]))
print("  Defender: " + str(d[0]) + "-" + str(d[1]))
a_lost_unit=0
d_lost_unit=0
while len(d)>0:
    if max(d)>=max(a):
        a_lost_unit +=1
    else:
        d_lost_unit +=1
    a.remove(max(a))
    d.remove(max(d))
print("Outcome:")
print("  Attacker: Lost "+ str(a_lost_unit) + " units" )
print("  Defender: Lost "+ str(d_lost_unit) + " units" )
