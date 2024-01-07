def possible_triangle_check(a, b, c):

    sides = [a, b, c]
    
    longest_side = max(sides)

    sides.remove(longest_side)

    if sum(sides) > longest_side:
        return True
    else:
        return False


def main():

    while True:
        a = float(input("Enter length of side a: "))
        b = float(input("Enter length of side b: "))
        c = float(input("Enter length of side c: "))

        is_possible = possible_triangle_check(a, b, c)

        if is_possible:
            print("The triangle is possible ")
            break
        else:
            print("The triangle is not possible")
            

    if  a == b or a == c or b == c:
        print("The triangle is isosceles")
    elif a == b == c:
        print("The triangle is equillateral")
    else:
        print("The triangle is scalene")

if __name__ == '__main__':
    main()
