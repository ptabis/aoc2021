with open("input.txt", "r") as f:
    horizontal = 0
    depth = 0
    aim = 0

    lines = f.readlines()
    lines = [line.strip().split(" ") for line in lines]
    
    for line in lines:
        if line[0] == "up":
            aim -= int(line[1])
        if line[0] == "down":
            aim += int(line[1])
        if line[0] == "forward":
            horizontal += int(line[1])
            depth += (int(line[1]) * aim)

    print(horizontal*depth)