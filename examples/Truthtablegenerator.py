# Truth Table Generator for Boolean Expressions

def generate_table(expression):
    """Generates and prints a truth table for a given Boolean expression."""

    variables, num_vars = number_of_inputs(expression)

    print(f"\nGenerating a Truth Table for the expression: {expression}")
    print("=" * (num_vars * 4 + 6))  # Dynamic width based on variables

    # Print Header
    for var in variables:
        print(f"| {var} ", end="")
    print("| Y |")  # Output column

    print("=" * (num_vars * 4 + 6))  # Separator line

    # Generate all possible input combinations (Binary Counting)
    values = [0] * num_vars  # Start with all 0s

    while True:
        # Create a truth map for current values
        truth_map = {variables[i]: values[i] for i in range(num_vars)}

        # Evaluate the expression
        result = evaluate_expression(expression, truth_map)

        # Print row
        for bit in values:
            print(f"| {bit} ", end="")
        print(f"| {result} |")

        # Manually increment binary sequence
        for i in range(num_vars - 1, -1, -1):  # Start from the rightmost bit
            values[i] = 1 - values[i]  # Toggle bit (0 → 1, 1 → 0)
            if values[i] == 1:
                break  # Stop flipping after first 0 → 1 transition
        else:
            break  # If no 0 → 1 transition happened, we've reached the last row

    print("=" * (num_vars * 4 + 6))  # Final separator line


def number_of_inputs(expression):
    """Extracts unique input variables from the Boolean expression."""

    unique = []  # List to store unique variables
    signs = ["+", "'", " ", "(", ")"]  # Characters to ignore

    for char in expression:
        if char not in unique and char not in signs:
            unique.append(char)

    return sorted(unique), len(unique)  # Return sorted variables and count


def evaluate_expression(expression, truth_map):
    """Replaces variables with actual values and evaluates the Boolean expression."""

    # Replace variables with truth values
    exp = expression
    for var, val in truth_map.items():
        exp = exp.replace(var, str(val))

    # Handle NOT (A' → NOT A)
    while "'" in exp:
        index = exp.index("'")
        if index > 0:
            exp = exp[:index - 1] + str(1 - int(exp[index - 1])) + exp[index + 1:]


    # Handle implicit AND (e.g., "AB" → "A and B")
    i = 0
    while i < len(exp) - 1:
        if exp[i].isdigit() and exp[i + 1].isdigit():  # If two digits are adjacent, insert "and"
            exp = exp[:i + 1] + " and " + exp[i + 1:]
        i += 1

    # Replace OR (`+`) with `or`
    exp = exp.replace("+", " or ")

    # Evaluate and return result
    return eval(exp)


def main():
    is_running = True
    while is_running:
        expression1 = input("Please enter your expression or 'exit' to end: ").upper()
        if expression1 == "EXIT":
            print("The program has been terminated")
            is_running = False
        else:
            generate_table(expression1)



# Run the main function
if __name__ == "__main__":
    main()
