def str_to_morse_code(msg, key):

    # msg_list is a list where each element is each element in msg
    msg_list = [msg[i] for i in range(len(msg))]

    encoded_msg = ""

    for i in range(len(msg)):
        
        # from dict key, appends the morse code char that corresponds to the char at msg_list[i]
        if key[msg_list[i]] != "/":
            encoded_msg += key[msg_list[i]]
            encoded_msg += " "
        else:
            encoded_msg = encoded_msg[:-1] # removes the last character of the string VERY HELPFUL
            encoded_msg += key[msg_list[i]]

    if encoded_msg[-1] == " ":
        encoded_msg = encoded_msg[:-1]

    return encoded_msg
    # return msg_list

def morse_code_to_str(msg, key):

    morse_list = msg.split(" ") # this creates a list
    # print(morse_list)

    for i in range(len(morse_list)):
        if "/" in morse_list[i]:

            # print(f"morse_list[i]: {morse_list[i]}")
            split_chars = morse_list[i].split("/")
            # print(f"morse_list[i]: {morse_list[i]}")
            # print(f"split_chars: {split_chars}")

            split_chars.insert(len(split_chars) // 2, '/')
            # this reassigns the elements of split_chars into the list as regular elements somehow
            morse_list[i:i+1] = split_chars
            # print(f"morse_list[i]: {morse_list[i]}")

    morse_list = list(filter(None, morse_list))

    decoded_msg = ""

    for i in range(len(morse_list)):
        decoded_msg += key[morse_list[i]]

    return decoded_msg
    # return morse_list



def main():
    # each character on the left corresponds to a morse code character on the right
    # all the KEYS are on the left and their VALUES are on the right
    # you can only reference the left side and get the right side, not the other way around
    alpha_to_morse_code = {
        " ": "/", # space is replaced by a pipe
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--.."
    }

    morse_code_to_alpha = {
        "/": " ", # pipe is replaced by space
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z"
    }


    user_input = input("Enter your message: ").lower()
    encoded = str_to_morse_code(user_input, alpha_to_morse_code)
    print(f"Your encoded message: {encoded}")

    print("\n")

    user_input = input("Enter your message: ").lower()
    encoded = morse_code_to_str(user_input, morse_code_to_alpha) # type: ignore
    print(f"Your encoded message: {encoded}")

    # print(f"Your decoded message: {morse_code_to_str(encoded, morse_code_to_alpha)}")


if __name__ == '__main__':
    main()
