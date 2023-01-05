# Initial game 
gameInitialValue = 301

# Which dart is in play
dart1 = 0
dart2 = 0
dart3 = 0

# Players' scores
p1Score = gameInitialValue
p2Score = gameInitialValue

# Print players' scores
def printScores():
    print("Player 1's Score: " + str(p1Score) + "\tPlayer 2's Score: " + str(p2Score))
 
# Calculate dart score
def calcDartScore(segmentValue, multiplier):
    # input validation
    if segmentValue > 20 or segmentValue < 1:
        print("Error! Incorrect dart value!")
        return 0
    if multiplier > 3 or multiplier < 1:
        print("Error! Incorrect multiplier value!")
        return 0

    dartScore = 0
    if multiplier != 1:
        dartScore = segmentValue * multiplier
    else:
        dartScore = segmentValue
    return dartScore

def calcSet(dart1, dart2, dart3):
    setScore = dart1 + dart2 + dart3
    return setScore

# game   
while p1Score != 0 and p2Score != 0:
    printScores()
    turn = 0

    if turn == 0:
        print("\n\tPlayer 1:")
    elif turn == 1:
        print("\n\tPlayer 2:")

    dart1 = calcDartScore(int(input("Enter dart value 1: ")), int(input("Enter multiplier: ")))
    dart2 = calcDartScore(int(input("Enter dart value 2: ")), int(input("Enter multiplier: ")))
    dart3 = calcDartScore(int(input("Enter dart value 3: ")), int(input("Enter multiplier: ")))

    setScore = calcSet(dart1, dart2, dart3)

    if turn == 0:
        p1Score -= setScore
        turn = 1
    elif turn == 1:
        p2Score -= setScore
        turn = 0

if p1Score == 0:
    print("Congratulations Player 1! You Win!")
elif p2Score == 0:
    print("Congratulations Player 2! You Win!")


