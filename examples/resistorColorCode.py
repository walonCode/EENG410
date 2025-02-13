def colorCoder(arr_of_the_resistor_color):
    colorDigits = {
        "black" : 0,
        "brown": 1,
        "red":2,
        "orange":3,
        "yellow":4,
        "green":5,
        "blue":6,
        "violet":7,
        "gray": 8,
        "white":9,
    }

    colorMultiplier = {
        "black" : 1,
        "brown": 10,
        "red":100,
        "orange":1000,
        "yellow":10000,
        "green":100000,
        "blue":1000000,
        "violet":10000000,
        "gray": 100000000,
        "white":1000000000,
        "gold":0.1,
        "sliver":0.01
    }

    colorTolerance = {
        "black" : 0,
        "brown": 1,
        "red":2,
        "orange":3,
        "yellow":4,
        "green":5,
        "blue":6,
        "violet":7,
        "gray": 8,
        "white":9,
    }
    validArr = []
    if len(arr_of_the_resistor_color) != 0:
        return validArr.append(arr_of_the_resistor_color)

 