INPUT_FILE = "small_input.txt"

instructions = []

with open(INPUT_FILE, "r") as file:
    
    # Loop over each line in the file
    for line in file:
        # Remove the newline character at the end
        line = line.strip()

        if line == "":   #could be written as if not line:
            continue

        # Get the first character (R or L)
        direction = line[0]

        # Get the rest of the string (the number part)
        amount_str = line[1:]

        # Convert the number from string to integer
        amount = int(amount_str)

        instructions.append((direction, amount))

print(instructions)