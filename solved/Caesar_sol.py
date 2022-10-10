### Code César

from base64 import encode


def shift(letter: str, s: int) -> str:
    """Cette fonction permet de décaler la lettre donnée en paramètre (letter) selon le décalage (s).

    Args:
        letter (str): Lettre à décaler.
        s (int): Décalage.

    Returns:
        str: La lettre décalée.

    Examples:
        - shift("a", 3) == "d"
        - shift("a", -1) == "z"
        - shift("J", -42) == "T"
        - shift("v", 23) == "s"
    """

    if (letter.isupper()):
        return chr((ord(letter) + s - 65) % 26 + 65)
    else:
        return chr((ord(letter) + s - 97) % 26 + 97)

def encode_word(word: str, s: int) -> str:
    """ Cette fonction applique le décalage (s) à chaque lettre contenue dans le mot/phrase en paramètre (word).
        Attention ! Il ne faut pas encoder les espaces.

    Args:
        word (str): Mot ou phrase à encoder.
        s (int): Décalage.

    Returns:
        str: Le mot/la phrase décalée.

    Examples:
        - encode_word("Josh", -42) == "Tycr"
        - encode_word("Anismateur", 2) == "Cpkuocvgwt"
        - encode_word("Je sais pas trop quoi mettre comme example", 69) == "Av jrzj grj kifg hlfz dvkkiv tfddv vordgcv"
    """
    n = len(word)
    result = ""
    for i in range(n):
        if word[i] == ' ':
            result += ' '
        else:
            result += shift(word[i], s)
    return result

def decode_word(word: str, s: int) -> str:
    """ Cette fonction permet de décoder le message secret donné en paramètre (word) selon le décalage.
        Cette fonction ressemble beaucoup à la précédente, à une petite différence près. Pensez à bien gérer le cas des espaces !
    Args:
        word (str): Message à décoder.
        s (int): Décalage.

    Returns:
        str: Le message décodé.

    Examples: (oui, j'ai repris les mêmes qu'avant...)
        - decode_word("Tycr", -42) == "Josh"
        - decode_word("Cpkuocvgwt", 2) == "Anismateur"
        - encode_word("Av jrzj grj kifg hlfz dvkkiv tfddv vordgcv", 69) == "Je sais pas trop quoi mettre comme example"
    """
    n = len(word)
    result = ""
    for i in range(n):
        if word[i] == ' ':
            result += ' '
        else:
            result += shift(word[i], -s)
    return result