import csv
import xlwt
import sys
import helpers
import numbers

myTabfile = open("players.txt", "r")
myReadtab = csv.reader(myTabfile, delimiter='\t')


class Player:

    def __init__(self, number, firstname, lastname, position, abvPosition, fullClass, abbrClass, numClass, height, weight, hometown, batting, throwing):
        self.number = number
        self.firstname = firstname
        self.lastname = lastname
        self.position = position
        self.abvPosition = abvPosition
        self.fullClass = fullClass
        self.abbrClass = abbrClass
        self.numClass = numClass
        self.height = height
        self.weight = weight
        self.hometown = hometown
        self.batting = batting
        self.throwing = throwing


# set these according to what field the item is in.
playernumber = 0
playername = 1
playerposition = 3
pclass = 2
playerheight = 4
playerweight = 5
playerhometown = 6
batsThrows = 4
filename = sys.argv[1] + ".csv"
reverseName = sys.argv[2]
sport = sys.argv[3]

players = []
for x in range(0, 100):
    players.insert(x, Player("", "", "", "", "",
                             "", "", "", "", "", "", "", ""))

for row in myReadtab:
    PlayerInfo = '|'.join(row)
    SplitInfo = PlayerInfo.split('|')
    print(SplitInfo)

    # get number
    newPlayerNumber = helpers.GetField(SplitInfo, playernumber)

    # figure out name
    newPlayerName = ""
    if reverseName == True:
        nameRaw = helpers.GetField(SplitInfo, playername)
        newPlayerName = nameRaw.split(',')[1] + " " + nameRaw.split(',')[0]
    else:
        newPlayerName = helpers.GetField(SplitInfo, playername)

    newPlayerFirstname = newPlayerName.split(' ')[0]
    newPlayerLastname = newPlayerName.split(' ')[1]

    # position
    newPlayerPosition = helpers.GetField(SplitInfo, playerposition)

    if sport == 'Soccer':
        newPlayerPositionAbv = helpers.GetAbvPositionSoccer(newPlayerPosition)
        newPlayerPosition = helpers.GetPositionSoccer(newPlayerPosition)
    if sport == 'Volleyball':
        newPlayerPositionAbv = newPlayerPosition
        newPlayerPosition = helpers.GetPositionVolleyball(newPlayerPosition)
    else:
        newPlayerPositionAbv = newPlayerPosition

    # class
    playerclass = helpers.GetField(SplitInfo, pclass).replace('.', '').lower()
    newPlayerClassAbbr = helpers.GetClass(playerclass, True)
    newPlayerClassFull = helpers.GetClass(playerclass, False)
    newPlayerClassNum = helpers.GetNumberedClass(playerclass)

    # height
    newPlayerHeight = helpers.GetFormattedHeight(
        helpers.GetField(SplitInfo, playerheight))

    # weight
    newPlayerWeight = helpers.GetField(SplitInfo, playerweight)

    # hometown
    newPlayerHometown = helpers.GetFormattedHometown(
        helpers.GetField(SplitInfo, playerhometown))

    # baseball stuffs
    if sport == "Baseball":
        newPlayerBatting = helpers.GetBatting(
            helpers.GetField(SplitInfo, batsThrows))
        newPlayerThrowing = helpers.GetThrowingArm(
            helpers.GetField(SplitInfo, batsThrows))
    else:
        newPlayerBatting = " "
        newPlayerThrowing = " "

    errors = "Problem processing: "
    try:
        playerNumberIndex = int(SplitInfo[playernumber].strip())
        players.insert(playerNumberIndex, Player(newPlayerNumber, newPlayerFirstname, newPlayerLastname, newPlayerPosition, newPlayerPositionAbv,
                                                 newPlayerClassFull, newPlayerClassAbbr, newPlayerClassNum, newPlayerHeight, newPlayerWeight, newPlayerHometown, newPlayerBatting, newPlayerThrowing))

    except:
        errors = errors + "There was a problem with a player\n"


# open the file and write to it
f = open(filename, 'w')

for x in range(0, 100):
    # print players[x].lastname
    if sport == 'Soccer':
        playerString = str(x) + "," + str(players[x].number) + "," + players[x].firstname + "," + players[x].lastname + "," + players[x].abvPosition + \
            ',' + players[x].position + "," + players[x].height + ", ," + \
            players[x].abbrClass + ',"' + players[x].hometown + '"\n'
    elif sport == 'Volleyball':
        playerString = str(x) + "," + str(players[x].number) + "," + players[x].firstname + "," + players[x].lastname + "," + players[x].abvPosition + \
            ',' + players[x].position + "," + players[x].height + ", ," + \
            players[x].abbrClass + ',"' + players[x].hometown + '"\n'
    elif sport == 'Basketball':
        playerString = str(x) + "," + str(players[x].number) + "," + players[x].firstname + "," + players[x].lastname + "," + \
            players[x].position + "," + players[x].height + "," + players[x].weight + "," + \
            players[x].abbrClass + ',"' + players[x].hometown + '"\n'
    elif sport == 'Lacrosse':
        playerString = str(x) + "," + str(players[x].number) + "," + players[x].firstname + "," + players[x].lastname + ", ," + \
            players[x].position + ", ," + players[x].height + ", ," + \
            players[x].abbrClass + ',"' + players[x].hometown + '"\n'
    elif sport == 'Baseball':
        playerString = str(x) + "," + players[x].lastname + "," + players[x].firstname + "," + players[x].number + ", ," + players[x].position + "," + players[x].batting + \
            "," + players[x].throwing + ',' + players[x].hometown + ',' + \
            players[x].height + "," + players[x].weight + \
            "," + players[x].fullClass + '\n'
    else:
        playerString = str(x) + "," + str(players[x].number) + "," + players[x].firstname + "," + players[x].lastname + "," + players[x].position + \
            "," + players[x].height + "," + players[x].weight + ',"' + \
            players[x].hometown + '",' + players[x].numClass + "\n"
    f.write(playerString)

f.write(errors)
f.close()
