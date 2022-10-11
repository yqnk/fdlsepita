import random
from Game import *

def getSecret() -> str:
    n = len(dictionary)
    return dictionary[random.randint(0, n - 1)]

def replaceLetter(currentWord: str, secretWord: str, letter: str) -> str:
    result = ""
    n = len(secretWord)
    for i in range(n):
        if secretWord[i] == letter:
            result += letter
        else:
            result += currentWord[i]
    return result

def play():
    # Cette ligne initialise une partie avec un mot secret choisi grâce à la fonction que vous avez définie plus haut.
    game = Game(getSecret())
    while not game.isFinished():
        print(game)
        print("Mot actuel : " + game.currentWord)
        ipt = input("Rentrez une lettre : ").lower()
        if len(ipt) > 1:
            continue
        
        if ipt in game.secretWord:
            game.currentWord = replaceLetter(game.currentWord, game.secretWord, ipt)
        else:
            game.state += 1
        print("State : " + str(game.state))
        
    if game.isLost():
        print("Dommage tu as perdu !")
    elif game.isWon():
        print("Bien joué, tu as gagné !")

# play()
