def simple_reverse(msg):
    return msg[::-1]

print(simple_reverse("hello world"))

def vowels_and_consonants(msg):
    
    vowels = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"

    vowels_in_msg = ""
    consonants_in_msg = ""

    for i in range(len(vowels)):
        if vowels[i] in msg:
            vowels_in_msg += vowels[i]
    
    for i in range(len(consonants)):
        if consonants[i] in msg:
            consonants_in_msg += consonants[i]

    return f"vowels in message: {vowels_in_msg}\nconsonants in message: {consonants_in_msg}"

print(vowels_and_consonants("hello world"))
print(vowels_and_consonants("hello hello hello hi hi hi hi hi cat dog elephant giraffe coffee this is a long message"))

def is_palendrone(msg):
    return msg == msg[::-1]

print(is_palendrone("hello world"))
print(is_palendrone("racecar"))
print(is_palendrone("hannah"))