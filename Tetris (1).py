# List of Tetris scores (unsorted)
scores = [
    3600460, 1388900, 5435960, 4222920, 8063900, 1362703, 6529560, 2043580, 1390000, 1696224,
    1372600, 2535840, 2605320, 2275996, 11966100, 1472600, 1390780, 1768400, 1333731, 1317580,
    1777456, 4899280, 2790920, 1626880, 1476400, 29486164, 4570640, 1649100, 4890220, 6492500,
    1614120, 5157860, 1582980, 1357480, 2382340, 1532660, 2378832, 1316520, 2529080, 13793540,
    1386260, 1352620, 1442340, 1406260, 1705680, 12409180, 2281848, 3222400, 1349060, 2302480,
    1571120, 3067100, 3740500, 1606732, 2153480, 2011360, 1344740, 1371060, 1345420, 2373940,
    1702940, 2077552, 2108820, 1322485, 1404800, 2555620, 1405580, 4213540, 3835120, 6563440,
    1350742, 1537800, 1657560, 1333995, 1632505, 2743060, 1509751, 1554880, 1316540, 1323680,
    2433160, 1340460, 1659860, 1608500, 7220241, 1834120, 7081880, 1483360, 16700760, 1435280,
    1702640, 1371040, 1316900, 2114180, 1374100, 1412260, 1379220, 1319573, 1623160, 6787420
]
#1.
def highscore():
    largestNum = 0
    for number in scores:
        if number > largestNum:
            largestNum = number
    print(largestNum)
#2.
def lowscore(scores):
    lownum = scores[0]
    for number in scores:
        if number < lownum:
            lownum = number

    # Print the lowest number
    print(f"The lowest score is: {lownum}")

#3.
total = 0
for i in range(len(scores)):
    total = total + scores[i]
mass = total / 100

#4


food = int(input("What is your High Score?: "))
if food > 1316520:
    scores.append(food)   
    scores.remove(1316520)
else:
    print("Sorry your score is not high enough")





#main
highscore()
lowscore()
print(mass)
