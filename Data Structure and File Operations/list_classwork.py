# calculating the resistance for resistors in parallel
# formula (1/R1 + 1/R2 + 1/Rn) ** -1

def calculate_parallel_resistance(resistor):
    total_sum = sum(1/r for r in resistor)
    return  1/total_sum

def calculate_series_resistance(resistor):
    total_sum = sum(resistor)
    return total_sum



resistor = [1,2,3]
total_parallel_resistance = calculate_parallel_resistance(resistor)
total_series_resistance = calculate_series_resistance(resistor)

print(f'total parallel resistance = {total_parallel_resistance:.2f} ohms')
print(f'total series resistance {total_series_resistance} ohms')