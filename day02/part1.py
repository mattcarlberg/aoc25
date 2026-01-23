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
        if len(num_str)%2 == 0:
            mid = len(num_str)//2
            if num_str[:mid] == num_str[mid:]:
                total = total + j 
print(total)





