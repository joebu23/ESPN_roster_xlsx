def GetField(array, index):
    return array[index].strip()


def GetAbvPositionSoccer(position):
    if position.find('Goalkeeper') != -1:
        return 'GK'
    if position.find('Defender') != -1:
        return 'D'
    if position.find('Midfielder') != -1:
        return 'M'
    if position.find('Forward') != -1:
        return 'F'
    else:
        return position


def GetPositionSoccer(position):
    if position == 'GK':
        return 'Goalkeeper'
    if position == 'D':
        return 'Defender'
    if position == 'M':
        return 'Midfielder'
    if position == 'F':
        return 'Forward'
    if position == 'M/F':
        return 'Mid/Forward'
    if position == 'F/M':
        return 'Forward/Mid'
    else:
        return position


def GetPositionVolleyball(position):
    if position == 'DS':
        return 'Defensive Specialist'
    if position == 'L':
        return 'Libero'
    if position == 'MB':
        return 'Middle Blocker'
    if position == 'S':
        return 'Setter'
    if position == 'OH':
        return 'Outside Hitter'
    if position.find('DS') != -1:
        return 'Defensive Specialist'
    else:
        return position


def FixState(hometown):
    if hometown.find('Mich.') != -1:
        return hometown.replace('Mich.', 'MI')
    if hometown.find('Ohio') != -1:
        return hometown.replace('Ohio', 'OH')
    if hometown.find('Ill.') != -1:
        return hometown.replace('Ill.', 'IL')
    if hometown.find('Ind.') != -1:
        return hometown.replace('Ind.', 'IN')
    if hometown.find('Fla.') != -1:
        return hometown.replace('Fla.', 'FL')
    if hometown.find('Ga.') != -1:
        return hometown.replace('Ga.', 'GA')
    if hometown.find('Ky.') != -1:
        return hometown.replace('Ky.', 'KY')
    if hometown.find('Calif.') != -1:
        return hometown.replace('Calif.', 'CA')
    if hometown.find('Wisc.') != -1:
        return hometown.replace('Wisc.', 'WI')
    if hometown.find('Wis.') != -1:
        return hometown.replace('Wis.', 'WI')
    if hometown.find('Pa.') != -1:
        return hometown.replace('Pa.', 'PA')
    if hometown.find('Kan.') != -1:
        return hometown.replace('Kan.', 'KS')
    if hometown.find('N.Y.') != -1:
        return hometown.replace('N.Y.', 'NY')
    if hometown.find('N.J.') != -1:
        return hometown.replace('N.J.', 'NJ')
    if hometown.find('Minn.') != -1:
        return hometown.replace('Minn.', 'MN')
    if hometown.find('Ala.') != -1:
        return hometown.replace('Ala.', 'AL')
    if hometown.find('Texas') != -1:
        return hometown.replace('Texas', 'TX')
    if hometown.find('Mo.') != -1:
        return hometown.replace('Mo.', 'MO')
    if hometown.find('N.C.') != -1:
        return hometown.replace('N.C.', 'NC')
    if hometown.find('Ariz.') != -1:
        return hometown.replace('Ariz.', 'AZ')
    if hometown.find('Neb.') != -1:
        return hometown.replace('Neb.', 'NE')
    if hometown.find('Iowa') != -1:
        return hometown.replace('Iowa', 'IA')

    return hometown


def GetClass(playerclass, abbr):
    if playerclass.find('fr') != -1:
        if abbr:
            return "FR"
        else:
            return "Freshman"
    elif playerclass.find('so') != -1:
        if abbr:
            return "SO"
        else:
            return "Sophomore"
    elif playerclass.find('jr') != -1:
        if abbr:
            return "JR"
        else:
            return "Junior"
    elif playerclass.find('sr') != -1:
        if abbr:
            return "SR"
        else:
            return "Senior"
    else:
        return playerclass.capitalize()


def GetNumberedClass(playerclass):
    playerclass = playerclass.lower()
    if playerclass == 'fr':
        return "1"
    elif playerclass == 'fr.':
        return "1"
    elif playerclass == 'so':
        return "2"
    elif playerclass == 'r-so':
        return "2"
    elif playerclass == 'so.':
        return "2"
    elif playerclass == 'jr':
        return "3"
    elif playerclass == 'jr.':
        return "3"
    elif playerclass == 'r-jr':
        return "3"
    elif playerclass == 'sr':
        return "4"
    elif playerclass == 'sr.':
        return "4"
    elif playerclass == 'r-sr':
        return "4"
    elif playerclass == 'gr':
        return "4"
    elif playerclass == 'r-fr':
        return "1"
    elif playerclass == 'rfr':
        return "1"
    else:
        return "0"


def GetFormattedHeight(heightString):
    height = heightString.replace('-', "'", 1)
    return height + '"'


def GetFormattedHometown(hometownString):
    if hometownString.find('/') != -1:
        hometownString = hometownString.split("/")[0].strip()

    hometownString = hometownString.replace('-', ',')

    return FixState(hometownString)


def GetThrowingArm(batsThrows):
    throws = batsThrows.split('/')[1]
    return throws


def GetBatting(batsThrows):
    bats = batsThrows.split('/')[0]
    return bats
