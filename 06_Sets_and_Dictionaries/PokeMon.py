from collections import defaultdict

s = input()
dPlayers = defaultdict(set)
dDecks = defaultdict(set)
iMax = 0
result = []

while s:
    if (s[0].isdigit()):
        number, cardName = s.split(' / ')
        dDecks[number].add(cardName)
    else:
        playerName, numDeck = s.split(' / ')
        dPlayers[playerName].add(numDeck)
    s = input()

for playerName, setNumDeck in dPlayers.items():
    curDeck = set()
    for elem in setNumDeck:
        curDeck = curDeck.union(dDecks[elem])
    if (iMax < len(curDeck)):
        iMax = len(curDeck)
        result = [playerName]
    elif (iMax == len(curDeck)):
        result.append(playerName)

sortRes = sorted(result)

for curPlayer in sortRes:
    print(curPlayer) 