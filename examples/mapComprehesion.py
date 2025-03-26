colorTolerance = {
    "brown": 1, "red": 2, "green": 0.5, "blue": 0.25,
    "violet": 0.1, "gray": 0.05, "gold": 5, "silver": 10
}

reversedColorTolerance = {key:value for value, key in colorTolerance.items()}

print(colorTolerance.keys())
# print(reversedColorTolerance)