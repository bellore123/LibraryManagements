records = []

while True:
    line = input()
    if not line:
        break
    name, age, height = line.split(",")
    records.append((name, age, height))

# Sorting by name, then age, then height
records.sort(key=lambda x: (x[0], int(x[1]), int(x[2])))

print(records)
