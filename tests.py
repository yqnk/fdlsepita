import Game, Hangman, Caesar

# region asserts
def assert_eq(a, b):
    return a == b
# endregion

# region tests
tcaesar = {
    "shift": [
        [('a', 7), 'h'],
        [('v', 47), 'q'],
        [('C', -9), 'T'],
        [('k', -29), 'h'],
        [('a', 26), 'a'],
        [('z', -26), 'z'],
    ],
    "encode_word": [
        [("Epita", 5), "Junyf"],
        [("Epitech", -5), "Zkdozxc"],
        [("Dans la jungle terrible jungle", 42), "Tqdi bq zkdwbu juhhyrbu zkdwbu"],
        [("cHaNsOnNeTtE", 14), "qVoBgCbBsHhS"],
        [("Anis", -9), "Rezj"],
        [("Sani", 78), "Sani"],
    ],
    "decode_word": [
        [("OIEUlkDOI", -80), "QKGWnmFQK"],
        [("uiuiis uuq Q", -80), "wkwkku wws S"],
        [("Jxu Edu Fyusu yi huqb", 42), "The One Piece is real"],
        [("non je ne pense vraiment pas", 12), "bcb xs bs dsbgs jfowasbh dog"],
        [("terinakopilaptieEA", 77), "ufsjoblpqjmbqujfFB"],
        [("zvnkjmondondioczbvhz", -5), "easportsitsinthegame"],
    ]
}
tgame = {
    "iswon": [
        [("epita", "epita"), True],
        [("p_u_ai__er", "poulailler"), False],
        [("ep_t_", "epita"), False],
        [("____", "joie"), False],
        [("malheur", "malheur"), True],
    ],
    "islost": [
        (19, True),
        (8, True),
        (7, True),
        (5, False),
        (0, False),
    ],
    "isfinished": [
        [("epita", "epita", 5), True],
        [("epita", "epita", 18), True],
        [("ep_ta", "epita", 7), True],
        [("ep_ta", "epita", 1), False],
        [("t__c", "truc", 6), False],
        [("pub", "pub", 2), True],
    ]
}
thangman = {
    "replaceletter": [
        [("ep_ta", "epita", "i"), "epita"],
        [("ep_ta", "epita", "a"), "ep_ta"],
        [("pou_ai__er", "poulailler", "l"), "poulailler"],
        [("j__bo_", "jambon", "p"), "j__bo_"],
        [("bd__pit_", "bdeepita", "e"), "bdeepit_"],
    ]
}
# endregion

def main():
    a = input("\033[0;0mVoulez-vous effectuer les tests de Caesar.py ? [Y/n] ").lower()
    if a != "n":
        CaesarTests()
    b = input("\n\033[0;0mVoulez-vous effectuer les tests de Game.py ? [Y/n] ").lower()
    if b != "n":
        GameTests()
    c = input("\n\033[0;0mVoulez-vous effectuer les tests de Hangman.py ? [Y/n] ").lower()
    if c != "n":
        HangmanTests()

def valid(s: str) -> None:
    print(f"\033[1;32m{s}")

def invalid(s: str) -> None:
    print(f"\033[1;91m{s}")

def pprint(r: bool, s: str) -> None:
    if r:
        valid(s)
    else:
        invalid(s)

def CaesarTests():
    print("\033[0;0m--- Caesar ---")
    shiftscore, encodescore, decodescore = 0, 0, 0
    print("\n\033[0;0mshift :")
    for i in range(6):
        a, b = tcaesar["shift"][i][0][0], tcaesar["shift"][i][0][1]
        out, expected = Caesar.shift(a, b), tcaesar["shift"][i][1]
        cond = assert_eq(out, expected)
        shiftscore += int(cond)
        pprint(cond, f"{out}\t{'[ok]' if cond else f'| Expected : {expected}'} ({shiftscore}/6)")
    
    print("\n\033[0;0mencode_word :")
    for i in range(6):
        a, b = tcaesar["encode_word"][i][0][0], tcaesar["encode_word"][i][0][1]
        out, expected = Caesar.encode_word(a, b), tcaesar["encode_word"][i][1]
        cond = assert_eq(out, expected)
        encodescore += int(cond)
        pprint(cond, f"{out}\t{'[ok]' if cond else f'| Expected : {expected}'} ({encodescore}/6)")

    print("\n\033[0;0mdecode_word :")
    for i in range(6):
        a, b = tcaesar["decode_word"][i][0][0], tcaesar["decode_word"][i][0][1]
        out, expected = Caesar.decode_word(a, b), tcaesar["decode_word"][i][1]
        cond = assert_eq(out, expected)
        decodescore += int(cond)
        pprint(cond, f"{out}\t{'[ok]' if cond else f'| Expected : {expected}'} ({decodescore}/6)")

def GameTests():
    print('\033[0;0m--- Game ---')
    iwscore, ilscore, ifscore = 0, 0, 0
    
    print("\n\033[0;0misWon :")
    for i in range(5):
        a, b = tgame["iswon"][i][0][0], tgame["iswon"][i][0][1]
        g = Game.Game(b)
        g.currentWord = a
        expected = tgame["iswon"][i][1]
        cond = assert_eq(g.isWon(), expected)
        iwscore += int(cond)
        pprint(cond, f"{g.isWon()}\t{'[ok]' if cond else f'| Expected : {expected}'} ({iwscore}/5)")
    
    print("\n\033[0;0misLost :")
    for i in range(5):
        a = tgame["islost"][i][0]
        g = Game.Game("yan")
        g.state = a
        expected = tgame["islost"][i][1]
        cond = assert_eq(g.isLost(), expected)
        ilscore += int(cond)
        pprint(cond, f"{g.isLost()}\t{'[ok]' if cond else f'| Expected : {expected}'} ({ilscore}/5)")
    
    print("\n\033[0;0misFinished :")
    for i in range(6):
        a, b, c = tgame["isfinished"][i][0][0], tgame["isfinished"][i][0][1], tgame["isfinished"][i][0][2]
        g = Game.Game(b)
        g.currentWord = a
        g.state = c
        expected = tgame["isfinished"][i][1]
        cond = assert_eq(g.isFinished(), expected)
        ifscore += int(cond)
        pprint(cond, f"{g.isWon()}\t{'[ok]' if cond else f'| Expected : {expected}'} ({ifscore}/6)")

def HangmanTests():
    print('\033[0;0m--- Hangman ---')
    rlscore = 0
    print("\n\033[0;0mreplaceLetter :")
    for i in range(5):
        cw, sw, letter = thangman["replaceletter"][i][0][0], thangman["replaceletter"][i][0][1], thangman["replaceletter"][i][0][2]
        out, expected = Hangman.replaceLetter(cw, sw, letter), thangman["replaceletter"][i][1]
        cond = assert_eq(out, expected)
        rlscore += int(cond)
        pprint(cond, f"{out}\t{'[ok]' if cond else f'| Expected : {expected}'} ({rlscore}/5)")

if __name__ == "__main__":
    main()
    print("\033[0;0m")