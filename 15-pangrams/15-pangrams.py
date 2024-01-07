import re

def is_pangram_regex(msg):

    if re.match("^(?=.*a)(?=.*b)(?=.*c)(?=.*d)(?=.*e)(?=.*f)(?=.*g)(?=.*h)(?=.*i)(?=.*j)(?=.*k)(?=.*l)(?=.*m)(?=.*n)(?=.*o)(?=.*p)(?=.*q)(?=.*r)(?=.*s)(?=.*t)(?=.*u)(?=.*v)(?=.*w)(?=.*x)(?=.*y)(?=.*z).*$", msg, re.IGNORECASE):
        return True
    else:
        return False

print(is_pangram_regex("The quick brown fox jumps over the lazy dog"))
print(is_pangram_regex("By Jove, my quick study of lexicography won a prize!"))
print(is_pangram_regex("Stop posting about Among Us! I'm tired of seeing it!")) 

def is_pangram(msg):
    
    msg = msg.lower()

    return "a" in msg and "b" in msg and "c" in msg and "d" in msg and "e" in msg and "f" in msg and "g" in msg and "h" in msg and "i" in msg and "j" in msg and "k" in msg and "l" in msg and "m" in msg and "n" in msg and "o" in msg and "p" in msg and "q" in msg and "r" in msg and "s" in msg and "t" in msg and "u" in msg and "v" in msg and "w" in msg and "x" in msg and "y" in msg and "z" in msg

print("\n")
print(is_pangram("The quick brown fox jumps over the lazy dog"))
print(is_pangram("By Jove, my quick study of lexicography won a prize!"))
print(is_pangram("Stop posting about Among Us! I'm tired of seeing it!"))
