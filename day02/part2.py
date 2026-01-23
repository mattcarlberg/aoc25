def made_from_repeated_sequence(text):

    for i in range(1, len(text)//2+1):
        sequence = text[:i]
        if text.count(sequence)*len(sequence) == len(text):
            return True
    return False




INPUT_FILE = "large_input.txt"
with open(INPUT_FILE) as file:
    line = next(file).strip()

range_strings = line.split(",")
ranges = [tuple(map(int, r.split("-"))) for r in range_strings]


total = 0 
for r in ranges: 
    start = r[0]
    end = r[1]
    for j in range(start, end+1):
        num_str = str(j)
        if made_from_repeated_sequence(num_str):
            total = total + j

print(total)







