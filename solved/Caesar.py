### Code César

def shift(letter: str, s: int) -> str:
    if (letter.isupper()):
        return chr((ord(letter) + s - 65) % 26 + 65)
    else:
        return chr((ord(letter) + s - 97) % 26 + 97)

def encode_word(word: str, s: int) -> str:
    n = len(word)
    result = ""
    for i in range(n):
        if word[i] == ' ':
            result += ' '
        else:
            result += shift(word[i], s)
    return result

def decode_word(word: str, s: int) -> str:
    n = len(word)
    result = ""
    for i in range(n):
        if word[i] == ' ':
            result += ' '
        else:
            result += shift(word[i], -s)
    return result
