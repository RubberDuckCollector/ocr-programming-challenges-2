# distance must be miles and speed must be in miles per hour
# input time as seconds

digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def calc_speed(time1, time2, number_plate, distance=1):

    valid_plate = False

    if len(number_plate) == 8 and number_plate[0].isalpha() and number_plate[1].isalpha() and number_plate[4] == " " and int(number_plate[2]) in digits and int(number_plate[3]) in digits:
        valid_plate = True
    else:
        valid_plate = False
        
    
    if time1 == time2:
        speed_difference = 0
    elif time1 < time2:
        speed_difference = time2 - time1
    else:
        # difference is the time taken to go between cameras which is 1 mile
        speed_difference = time1 - time2

    average_speed = distance / speed_difference

    return average_speed * 3600, valid_plate # it's in miles per second so multiply for an hour

print(calc_speed(10, 12, "KL57 ABC"))