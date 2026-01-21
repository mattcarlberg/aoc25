INPUT_FILE = "large_input.txt"

commands = []

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

        commands.append((direction, amount))

count_zero = 0 
dial = 50 
for command in commands:
    direction = command[0] 
    amount = command[1]
    for i in range(amount):
        if direction == "R":
            dial = (dial + 1)%100
        else:
            dial = (dial - 1)%100
        if dial == 0:
            count_zero = count_zero + 1


print(count_zero)

