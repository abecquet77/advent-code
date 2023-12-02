import re

def part_one(data):
    result = 0
    for line in data:
        num = re.findall('\d', line)
        result += int(num[0] + num[-1])

    return result

def part_two(data):
    result = 0
    word_to_number = {
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for line in data:
        num = re.findall(
            '(?=(one|two|three|four|five|six|seven|eight|nine|\d))', line)
        first = word_to_number.get(num[0], num[0])
        last = word_to_number.get(num[-1], num[-1])
        result += int(first + last)

    return result

with open("2023/day_1/input") as f:
    data = f.read().split()

    print(part_one(data))

    print(part_two(data))
