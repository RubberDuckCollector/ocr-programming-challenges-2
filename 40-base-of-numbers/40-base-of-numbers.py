def convert_denary_to_hex(num):

    return hex(num)

print(convert_denary_to_hex(1982376437423))
            
def convert_to_base(number, base):
    if number == 0:
        return 0
    
    digits = "0123456789ABCDEF"

    result = ""
    while number > 0:
        remainder = number % base
        result = digits[remainder] + result
        number = number // base

    return result

num = int(input("enter number "))
base = int(input("enter the base to convert "))

result = convert_to_base(num, base)

print(f"the base-{base} representation of {num} is {result}")
