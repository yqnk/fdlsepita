HANGMAN_PICS = ['''
   +---+
       |
       |
       |
      ===\n''', '''
   +---+
   O   |
       |
       |
      ===\n''', '''
   +---+
   O   |
   |   |
       |
      ===\n''', '''
   +---+
   O   |
  /|   |
       |
      ===\n''', '''
   +---+
   O   |
  /|\  |
       |
      ===\n''', '''
   +---+
   O   |
  /|\  |
  /    |
      ===\n''', '''
   +---+
   O   |
  /|\  |
  / \  |
      ===\n''']

dictionary = [line.removesuffix('\n') for line in open('words.txt', 'r').readlines()]

class Game:
    def __init__(self, secretWord):
        self.secretWord = secretWord # le mot secret à deviner
        self.currentWord = ''.join(['_'] * len(secretWord)) # le mot actuel que l'utilisateur a trouvé. Exemple : 'ep_ta'
        self.state = 0
    
    def __str__(self):
        return HANGMAN_PICS[self.state]

    # Vous n'avez rien à modifier au dessus de cette ligne.

    def isWon(self) -> bool:
        return self.currentWord == self.secretWord

    def isLost(self) -> bool:
        return self.state >= len(HANGMAN_PICS)

    def isFinished(self) -> bool:
        return self.isWon() or self.isLost()