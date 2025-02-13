def colorCoder(arr_of_the_resistor_color: list[str]):
    colorDigits = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
    }

    colorMultiplier = {
        "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10_000,
        "green": 100_000, "blue": 1_000_000, "violet": 10_000_000, "gray": 100_000_000,
        "white": 1_000_000_000, "gold": 0.1, "sliver": 0.01
    }

    colorTolerance = {
        "brown": 1, "red": 2, "green": 0.5, "blue": 0.25,
        "violet": 0.1, "gray": 0.05, "gold": 5, "sliver": 10
    }

    
    if not arr_of_the_resistor_color:
        return "Invalid input: Empty array"

    validArr = arr_of_the_resistor_color  


    if len(validArr) == 4:
        firstValue = colorDigits.get(validArr[0], -1)
        secondValue = colorDigits.get(validArr[1], -1)
        multiplier = colorMultiplier.get(validArr[2], -1)
        tolerance = colorTolerance.get(validArr[3], "Unknown")

        if -1 in (firstValue, secondValue, multiplier):
            return "Invalid color in input"

        resistance = (firstValue * 10 + secondValue) * multiplier
        return f"Resistance: {resistance}Ω, Tolerance: ±{tolerance}%"

    elif len(validArr) == 5: 
        firstValue = colorDigits.get(validArr[0], -1)
        secondValue = colorDigits.get(validArr[1], -1)
        thirdValue = colorDigits.get(validArr[2], -1)
        multiplier = colorMultiplier.get(validArr[3], -1)
        tolerance = colorTolerance.get(validArr[4], "Unknown")

        if -1 in (firstValue, secondValue, thirdValue, multiplier):
            return "Invalid color in input"

        resistance = (firstValue * 100 + secondValue * 10 + thirdValue) * multiplier
        return f"Resistance: {resistance}Ω, Tolerance: ±{tolerance}%"

    else:
        return "Invalid band count. Only 4-band and 5-band resistors are supported."


def main():
    arr = ['red', 'violet', 'yellow', 'gold']  
    print(colorCoder(arr))

    arr2 = ['red', 'violet', 'black', 'yellow', 'gold']  
    print(colorCoder(arr2))

    arr3 = ['red', 'blue'] 
    print(colorCoder(arr3))


main()
