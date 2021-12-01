with open("input.txt", "r") as f:
    lines = f.readlines()
    increased = 0

    lines = [int(line.strip()) for line in lines]

    try:
        for i_line, line in enumerate(lines):
            first_sum = lines[i_line] + lines[i_line+1] + lines[i_line+2]
            second_sum = lines[i_line+1] + lines[i_line+2] + lines[i_line+3]
            if first_sum < second_sum:
                increased += 1
    except:
        print(increased)