INPUT_FILE = "small_input.txt"
with open(INPUT_FILE) as file:
    lines = [line.strip() for line in file if line.strip()]
print(lines)