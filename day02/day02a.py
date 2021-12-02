with open("input.txt", "r") as f:
    horizontal = 0
    depth = 0

    lines = f.readlines()
    lines = [line.strip().split(" ") for line in lines]
    
    for line in lines:
        if line[0] == "up":
            depth -= int(line[1])
        if line[0] == "down":
            depth += int(line[1])
        if line[0] == "forward":
            horizontal += int(line[1])

    print(horizontal*depth)