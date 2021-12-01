with open("input.txt", "r") as f:
    increased = 0
    first = 1
    for line in f:
        if first == 1:
            previous = int(line.strip())
            first = 0
            continue
        current = int(line.strip())
        if previous < current:
            increased += 1
        previous = current
    print(increased)