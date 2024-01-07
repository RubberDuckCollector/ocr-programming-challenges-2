def numbers():
    nums = []

    order = input("Ascending or descending order ")

    for i in range(10):
        n = int(input("Enter a number: "))
        nums.append(n)

    if order == "ascending":
        for i in range(len(nums)):
            print(nums[i])
    elif order == "descending":
        for i in reversed(range(len(nums))):
            print(nums[i])

def strings(msg):
    # strip() removes leading and trailing whitespace, and replace() removes spaces
    msg = msg.strip(" ").replace(" ", "").lower()

    msg = list(msg) # turn the parsed string into a list of chars
    msg.sort() # sort the chars alphabetically

    # join each element (i) of msg by a blank space into a string (in this case reassigned to msg)
    msg = "".join([i for i in msg]) # did this list comp by myself
    
    return msg

print(strings("My rabbit"))

def sentence_structure(msg):

    msg = msg.split(" ")

    msg.sort()

    for i in range(len(msg)):
        msg[i] = strings(msg[i])

    msg = " ".join([i for i in msg])

    return msg

print(sentence_structure("My rabbit"))