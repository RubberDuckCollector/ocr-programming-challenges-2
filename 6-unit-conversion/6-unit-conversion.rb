def length_convert(choice, value)
    if choice == 1
        return value / 1.60934
    elsif choice == 2
        return value * 1.60934
    end
end

def speed_convert(choice, value)
    if choice == 1
        return value / 1.60934
    elsif choice == 2
        return value * 1.60934
    end
end

def temp_convert(value, unit1, unit2) # C K OR F
    if unit1 == "C" and unit2 == "F" # celcius to farenheit
        return (value * 9/5) + 32
    elsif unit1 == "C" and unit2 == "K" # celcius to kelvin
        return value + 273.15
    elsif unit1 == "F" and unit2 == "C" # farenheit to celcius
        return (value - 32) * 5/9
    elsif unit1 == "F" and unit2 == "K" # farenheit to kelvin
        return (value - 32) * 5/9 + 273.15
    elsif unit1 == "K" and unit2 == "C" # kelvin to celcius
        return value - 273.15
    elsif unit1 == "K" and unit2 == "F" # kelvin to farenheit
        return (value - 273.15) * 9/5 + 32
    end
end


def main
    print "What unit do you want to convert? (length (km, miles), speed (mph, kmh), temperature (C, F, K)) "

    choice = gets.chomp

    if choice == "length"

        print "enter the value of the distance to convert: "
        length_value = gets.chomp.to_i

        print "do you want to convert km to miles (1) or miles to km? (2) "
        length_choice = gets.chomp.to_i

        if length_choice == 1
            puts length_convert(1, length_value)
        elsif length_choice == 2
            puts length_convert(2, length_value)
        end
    
    elsif choice == "speed"
        print "enter the value of the distance to convert: "
        speed_value = gets.chomp.to_i

        print "do you want to convert kmh to mph (1) or mph to kmh? (2) "
        speed_choice = gets.chomp.to_i

        if speed_choice == 1
            puts length_convert(1, speed_value)
        elsif speed_choice == 2
            puts length_convert(2, speed_value)
        end
    
    elsif choice == "temperature"
        print "enter the value of the temperature to convert: "
        temp_value = gets.chomp.to_f

        print "is this Celcius (C), farenheit (F), or kelvin (K) "
        temp_unit1 = gets.chomp.upcase

        print "convert to Celcius (C), farenheit (F), or kelvin (K) "
        temp_unit2 = gets.chomp.upcase

        if temp_unit1 == "C" and temp_unit2 == "F"
            puts temp_convert(temp_value, "C", "F")
        elsif temp_unit1 == "C" and temp_unit2 == "K"
            puts puts temp_convert(temp_value, "C", "K")
        elsif temp_unit1 == "F" and temp_unit2 == "C"
            puts temp_convert(temp_value, "F", "C")
        elsif temp_unit1 == "F" and temp_unit2 == "K"
            puts temp_convert(temp_value, "F", "K")
        elsif temp_unit1 == "K" and temp_unit2 == "C"
            puts temp_convert(temp_value, "K", "C")
        elsif temp_unit1 == "K" and temp_unit2 == "F"
            puts temp_convert(temp_value, "K", "F")
        
        elsif temp_unit1 == "C" and temp_unit2 == "C"
            puts "C to C does not change"
        elsif temp_unit1 == "K" and temp_unit2 == "K"
            puts "K to K does not change"
        elsif temp_unit1 == "F" and temp_unit2 == "F"
            puts "F to F does not change"
        end

    end
end

main()
