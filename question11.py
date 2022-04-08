# The Farm Problem

def animal_legs(chickens, cows, pigs):
    chicken_legs = chickens * 2
    cows_legs = cows * 4
    pigs_legs = pigs * 4
    total_legs = chicken_legs + cows_legs + pigs_legs
    return total_legs


total1 = animal_legs(int(input("How many chickens: ")), int(input("How many cows: ")), int(input("How many pigs: ")))
total2 = animal_legs(int(input("How many chickens: ")), int(input("How many cows: ")), int(input("How many pigs: ")))

print("The total number of animal's legs ", total1)
print("The total number of animal's legs ", total2)
