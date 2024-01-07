num_of_bottles = int(input("How many bottles are on the wall? "))

for i in reversed(range(1, num_of_bottles + 1)):
    if i == 0:
        print(f"{i} green bottles standing on the wall, if a bottle falls, there will be {i} green bottles standing on the wall")
    elif i == 1: # checking for the difference in spelling
        print(f"{i} green bottle standing on the wall, if it falls, there will be {i-1} green bottles standing on the wall")
    else:
        print(f"{i} green bottles standing on the wall, if a bottle falls, there will be {i-1} green bottles standing on the wall")
