def part_1():
    commands = []
    horizontal = 0
    depth = 0

    with open("day-2-input.txt") as file:
        for line in file:
            commands.append(line)

    for command in commands:
        number = command.split()
        number = int(number[1])
        if "forward" in command:
            horizontal += number
        elif "down" in command:
            depth += number
        else:
            depth -= number
    print(horizontal * depth)

def part_2():
    commands = []
    with open("day-2-input.txt") as file:
        for line in file:
            commands.append(line)

    horizontal = 0
    depth = 0
    aim = 0

    for command in commands:
        number = command.split()
        number = int(number[1])
        if "forward" in command:
            horizontal += number
            depth += (aim * number)
        elif "down" in command:
            aim += number
        else:
            aim -= number
    print(horizontal * depth)


part_1()
part_2()