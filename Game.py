### Game

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

### Vous n'avez rien à modifier au dessus de cette ligne. ###

    def isWon(self) -> bool:
        """ Cette fonction indique si la partie est gagnée ou non.
            Une partie est gagnée quand le mot du joueur est le même que le mot secret.

        Returns:
            bool: True ou False.
        """
        pass # remove

    def isLost(self) -> bool:
        """ Cette fonction indique si la partie est gagnée ou non.
            Une partie perdue quand le state actuel est supérieur ou égal à 7.

        Returns:
            bool: True ou False.
        """
        pass # remove

    def isFinished(self) -> bool:
        """ Cette fonction indique si la partie est terminée ou non.
            Une partie est terminée lorsque le joueur a soit gagné, soit perdu.

        Returns:
            bool: True ou False.
        """
        pass # remove