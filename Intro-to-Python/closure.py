# closure in python
# it the ability for an inner function to maintain access to an outer function,even after when the outer function has done executing

def makeMultiplier(multiplier):
    def multiplier_function(value):
        return value * multiplier
    return multiplier_function

def main():
    multiplier = makeMultiplier(5)
    print(multiplier(10))

main()
