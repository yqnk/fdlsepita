### Hangman

import random
from Game import *

def getSecret() -> str:
    """Cette fonction renvoie un mot choisi aléatoirement dans la liste de mots ("dictionary").

    Returns:
        str: Le mot choisi au hasard.
    
    Hint:
        Pour cette fonction, utilisez la variable "dictionary" prédéfinie par moi (celui qui a fait le sujet). Elle contient une liste d'une centaine de mots.
    """
    pass # remove

def replaceLetter(currentWord: str, secretWord: str, letter: str) -> str:
    """Cette fonction prend trois paramètres et remplace les lettres dans le mot demandé. Si la lettre (letter) n'est pas présente dans le mot (secretWord), rien ne se passe.

    Args:
        currentWord (str): le mot dans lequel il faut remplacer.
        secretWord (str): le mot de référence.
        letter (str): la lettre que l'on va remplacer.

    Returns:
        str: Renvoie le mot (currentWord) avec les modifications appliquées. Si la lettre n'est pas présente ou déjà mise, rien ne se passe.

    Examples:
        - replaceLetter('_anger', 'manger', 'm') = 'manger'
        - replaceLetter('_n_n_s', 'ananas', 'a') = 'ananas'
        - replaceLetter('_anger', 'manger', 'z') = '_anger'
        - replaceLetter('ho__e', 'homme', 'm') = 'homme'
        - replaceLetter('b_te_u', 'bateau', 'p') = 'b_te_u'
        - replaceLetter('_anger', 'manger', 'a') = '_anger'

    Hint:
        On sait que (secretWord) et (currentWord) sont forcément de même longueur.

    Constraints:
        Evitez d'utiliser la fonction (str.replace()) prédéfinie en python. 
        Et oui, c'est comme ça, il existe des outils mais à Epita on doit faire les choses par soit même de temps en temps.
    """
    pass # remove

def play():
    """
        Cette fonction permet de lancer le jeu.
        Tant que la partie n'est pas finie, on effectue ces étapes :
            1)  On affiche l'état de la partie. (game.state)
            2)  On affiche le mot actuel (game.currentWord)
            3)  On récupère une lettre de la part du joueur.
                Si la donnée rentrée fait plus d'une lettre, alors on recommence.
                Si la donnée rentrée est en majuscule, on la récupère en miniscule via la fonction str.lower().
                    Example :
                        "saLUt".lower() = "salut"
            4)  On vérifie que la lettre rentrée est dans le mot secret (game.secretWord).
                Si oui, on remplace grâce à la fonction (replaceLetter), sinon on augmente la valeur de (game.state) de 1.

        Hint:
            Pour avoir l'affichage de l'état de la partie, vous pouvez tout simplement effectuer : "print(game)".
    """
    # Cette ligne initialise une partie avec un mot secret choisi grâce à la fonction que vous avez définie plus haut.
    game = Game(getSecret())
    pass # remove
    
    """
        Enfin, si la partie est perdue affichez "Dommage, tu as perdu !", si la partie est gagnée affichez "Bien joué, tu as gagné !".
    """
    pass # remove

# play() # uncomment to play