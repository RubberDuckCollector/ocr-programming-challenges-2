def add_year(year):
    
    year = str(year)

    year = list(map(int, year))

    return sum(year)

print(add_year(2015))


def guess(year):

    year = str(year)

    year_digits = sum(list(map(int, year)))

    attempt = 1

    while attempt < 4:
        guess = int(input("guess an integer "))

        if year_digits % guess == 0:
            print("correct")
            return
        else:
            print("incorrect")
            attempt += 1

    print("you couldn't get it in 3 attempts or fewer")
    return
    
guess(2015)
