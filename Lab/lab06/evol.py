import random, time
# Maker function will give you the list of generation
def maker(a,b):# a = object num, b = their gen num
    sub = []
    result = []
    for i in range(a):
        for j in range(b):
            sub.append(random.randrange(4))
        result.append(sub)
        sub = []
    return result

def chance(a):# a is percentage.
    num = random.random()

    if num <= float(a)/100:
        return 1
    else:
        return 0

def evol(evlist,a,b,mutchance,mutnum):# evlist = parents list, a and b is same with maker's
    result = []
    son = []
    for i in evlist:
        result.append(i)
    if a-len(evlist) == 0:
        return 0
    # Making son {
    for i in range(a-len(evlist)):
        for j in range(b):
            if chance(50)==1:
                son.append(evlist[0][j])
            else:
                son.append(evlist[1][j])
        result.append(son)
        son = []
    # } Making son
    # Mutant {
    if chance(mutchance)==1:
        for hh in range(mutnum):
            mutpos1 = random.randrange(a)
            mutpos2 = random.randrange(b)
            if result[mutpos1][mutpos2] == 0:
                result[mutpos1][mutpos2] = random.randrange(1,4)
            else:
                result[mutpos1][mutpos2] = random.randrange(0,4)
    #    print 'MUTANT!!!'*1000
    # } Mutant
    return result
