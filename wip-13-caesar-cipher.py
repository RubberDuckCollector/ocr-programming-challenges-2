def caesar_cipher(msg, offset):

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    new_msg = ""

    msg = msg.lower()

    for i in range(len(msg)):

        try:
            if msg[i] == " ":
                new_msg += " "
            else:
                new_letter = (alphabet.index(msg[i]) + offset) % 26
                new_msg += alphabet[new_letter]
        except ValueError:
            new_msg += msg[i]

    return new_msg

# print(caesar_cipher("mary had a little lamb", -3))

# print(caesar_cipher("HELLO WORLD", 11))
# print(caesar_cipher("hello world", 11))
# print(caesar_cipher("according to all known laws of aviation, there is no way a bee should be able to fly.", 11))

for i in range(0, 26):
    print(caesar_cipher("BRXFD QQRWO RVHDK RPLQJ SLJHR Q.LIB RXUKR PLQJS LJHRQ GRHVQ RWFRP HEDFN ,WKHQ ZKDWB RXKDY HORVW LVDSL JHRQ.", i))
    # print(caesar_cipher("fdwfk wkh sljhrq", i))
    # print(caesar_cipher("lnnzcotyr ez lww vyzhy wlhd zq lgtletzy, espcp tl yz hlj l mpp dszfwo mp lmwp ez qwj.", i))
    