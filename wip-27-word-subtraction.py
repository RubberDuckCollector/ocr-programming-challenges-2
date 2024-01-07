def convert_to_ascii(msg):

    msg_list = [ord(msg[i]) for i in range(len(msg))]

    return sum(msg_list)

def repeated_letters(word1, word2):

    word1 = list(word1)
    word2 = list(word2)

    print(word1 + word2)

    # return word3, word4

def main():

    msg1 = "hello world"

    num1 = convert_to_ascii(msg1)
    print(num1)

    msg2 = "aaaaldkjfkajfsd"
    
    num2 = convert_to_ascii(msg2)
    print(num2)

    print(num1 - num2)


    repeated_letters("fish", "tin")


if __name__ == '__main__':
    main()
