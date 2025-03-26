def valueCoder(arr_of_resistor_value: list[int]):
    colorDigits = {
        "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
        "green": 5, "blue": 6, "violet": 7, "gray": 8, "white": 9
    }

    colorMultiplier = {
        "black": 1, "brown": 10, "red": 100, "orange": 1000, "yellow": 10_000,
        "green": 100_000, "blue": 1_000_000, "violet": 10_000_000, "gray": 100_000_000,
        "white": 1_000_000_000, "gold": 0.1, "silver": 0.01
    }

    colorTolerance = {
        "brown": 1, "red": 2, "green": 0.5, "blue": 0.25,
        "violet": 0.1, "gray": 0.05, "gold": 5, "silver": 10
    }

    # Reverse mappings for decoding
    reverseColorDigits = {v: k for k, v in colorDigits.items()}
    reverseColorMultiplier = {v: k for k, v in colorMultiplier.items()}
    reverseColorTolerance = {v: k for k, v in colorTolerance.items()}

    if not arr_of_resistor_value:
        return "Invalid input"

    validArr = arr_of_resistor_value

    if len(validArr) == 4:
        firstColor = reverseColorDigits.get(validArr[0], "Invalid")
        secondColor = reverseColorDigits.get(validArr[1], "Invalid")
        multiplierColor = reverseColorMultiplier.get(validArr[2], "Invalid")
        toleranceColor = reverseColorTolerance.get(validArr[3], "Unknown")

        if "Invalid" in (firstColor, secondColor, multiplierColor):
            return "Invalid number in input"

        return [firstColor, secondColor, multiplierColor, toleranceColor]

    elif len(validArr) == 5:
        firstColor = reverseColorDigits.get(validArr[0], "Invalid")
        secondColor = reverseColorDigits.get(validArr[1], "Invalid")
        thirdColor = reverseColorDigits.get(validArr[2], "Invalid")
        multiplierColor = reverseColorMultiplier.get(validArr[3], "Invalid")
        toleranceColor = reverseColorTolerance.get(validArr[4], "Unknown")

        if "Invalid" in (firstColor, secondColor, thirdColor, multiplierColor):
            return "Invalid number in input"

        return [firstColor, secondColor, thirdColor, multiplierColor, toleranceColor]

    else:
        return "Invalid band count. Only 4-band and 5-band resistors are supported."


def main():
    arr = [1, 3, 1000, 5]  # Example input
    print(valueCoder(arr))  # Should return color names

main()
