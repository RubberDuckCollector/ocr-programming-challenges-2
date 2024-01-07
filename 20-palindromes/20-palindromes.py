def palindrome(msg):
    return msg[::-1] == msg

def main():
    print(palindrome("racecar"))
    print(palindrome("hello world"))

if __name__ == '__main__':
    main()