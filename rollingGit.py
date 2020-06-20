from random import choice, randint, shuffle

rollstats = []
findlowest = []

#A standard d6
def d6(quant=1):
    die = 0
    for i in range(0,quant):
        die += randint(1,6)
    return die
#A d6 where a 1 cannot be rolled
def d6no1s(quant=1):
    die = 0
    for i in range(0,quant):
        die += randint(2,6)
    return die
#A standard d20
def d20(quant=1):
    die = 0
    for i in range(0,quant):
        die += randint(1,20)
    return die
#A "cheater" d20 where the 1 and 2 are replaced with a 19 and 20
def d20cheater(quant=1):
    die = 0
    for i in range(0,quant):
        die += choice([20,19,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    return die
#################################################

#Chooses a random rolling method
def randomRollMethod():
    picker = randint(0,10)
    if picker == 10:
        return roll3d6()
    elif picker == 9:
        return roll4d6()
    elif picker == 8:
        return roll4d6_8x()
    elif picker == 7:
        return roll4d6nosub8()
    elif picker == 6:
        return roll4d6nosub8v2()
    elif picker == 5:
        return roll4d6musthave15()
    elif picker == 4:
        return roll4d6over70()
    elif picker == 3:
        return roll4d6onlyone16plus()
    elif picker == 2:
        return roll2d6plus6()
    elif picker == 1:
        return rolld20()
    else:
        return rolld20cheater()

#################################################

#roll 3d6
def roll3d6():
    rollstats.clear()
    for i in range(0,6):
        rollstats.append(d6(3))
    return rollstats

#roll 4d6 and drop the lowest roll in each set
def roll4d6():
    rollstats.clear()
    for i in range(0,6):
        findlowest.clear()
        for i in range(0,4):
           findlowest.append(d6())
        findlowest.sort()
        findlowest.pop(0)
        rollstats.append(sum(findlowest))
    return rollstats

#roll 4d6 and drop the lowest roll in each set eight times
#then drop the lowest two values overall
def roll4d6_8x():
    rollstats.clear()
    for i in range(0,8):
        findlowest.clear()
        for i in range(0,4):
            findlowest.append(d6())
        findlowest.sort()
        findlowest.pop(0)
        rollstats.append(sum(findlowest))
    rollstats.sort()
    del rollstats[0:2]
    shuffle(rollstats)
    return rollstats

#Roll 4d6, drop the lowest die and re-roll any total that is below 8.
def roll4d6nosub8():
    rollstats.clear()
    while len(rollstats) < 6:
        findlowest.clear()
        for i in range(0,4):
            findlowest.append(d6())
        findlowest.sort()
        findlowest.pop(0)
        rollstats.append(sum(findlowest))
        if rollstats[-1] < 8:
            rollstats.pop(-1)
    return rollstats

#Roll 4d6, drop the lowest die and swap any total below 8 with an 8.
def roll4d6nosub8v2():
    rollstats.clear()
    for i in range(0,6):
        findlowest.clear()
        for i in range(0,4):
            findlowest.append(d6())
        findlowest.sort()
        findlowest.pop(0)
        rollstats.append(sum(findlowest))
        if rollstats[-1] < 8:
            rollstats[-1] = 8
    return rollstats

#Roll 4d6, drop the lowest die but reroll the entire collection if
#no total is above 15.
def roll4d6musthave15():
    rollstats.clear()
    for i in range(0,6):
        findlowest.clear()
        for i in range(0,4):
            findlowest.append(d6())
        findlowest.sort()
        findlowest.pop(0)
        rollstats.append(sum(findlowest))
    if any(num > 15 for num in rollstats):
        pass
    else:
        roll4d6musthave15()
    return rollstats

#Roll 4d6, drop the lowest die and reroll the lowest total until the
#cumulative total value is over 70
def roll4d6over70():
    rollstats.clear()
    for i in range(0,6):
        findlowest.clear()
        for i in range(0,4):
            findlowest.append(d6())
        findlowest.sort()
        findlowest.pop(0)
        rollstats.append(sum(findlowest))
    if sum(rollstats) < 70:
        roll4d6over70()
    return rollstats

#Roll 4d6, reroll 1s and drop the lowest die but
#only one stat can be 16 or higher.
def roll4d6onlyone16plus():
    rollstats.clear()
    for i in range(0,6):
        findlowest.clear()
        for i in range(0,4):
            findlowest.append(d6no1s())
        findlowest.sort()
        findlowest.pop(0)
        rollstats.append(sum(findlowest))
    if any(num >= 16 for num in rollstats):
        counter = 0
        for number in rollstats:
            if number >= 16:
                counter += 1
                if counter > 1:
                    roll4d6onlyone16plus()
    return rollstats

#Roll 2d6+6
def roll2d6plus6():
    rollstats.clear()
    for i in range(0,6):
        rollstats.append(d6(2)+6)
    return rollstats

#Roll 1d20 for each stat
def rolld20():
    rollstats.clear()
    for i in range(0,6):
        rollstats.append(d20())
    return rollstats

#Roll a cheater d20 for each stat
def rolld20cheater():
    rollstats.clear()
    for i in range(0,6):
        rollstats.append(d20cheater())
    return rollstats
