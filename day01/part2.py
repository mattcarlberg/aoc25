INPUT_FILE = "large_input.txt"
with open(INPUT_FILE) as file:
    lines = [line.strip() for line in file if line.strip()]
commands = [(l[0],int(l[1:])) for l in lines]


direction_map = {"L": -1, "R": 1}
dial = 50
count_zero = 0

for direction, amount in commands:
    for _ in range(amount):
        dial = (dial + direction_map[direction]) % 100
        if dial == 0:
            count_zero += 1
print(count_zero)


