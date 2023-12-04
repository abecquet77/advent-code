import re

def part_one():
    result = 0
    with open("2023/day_4/input") as f:
        for line in f.read().split('\n'):
            numbers = line.split("|", 1)[0].split(":", 1)[1]
            numbers_list = set(re.findall('\d+', numbers))
            winners = line.split("|", 1)[1]
            winners_list = set(re.findall('\d+', winners))

            numbers_have = list(numbers_list.intersection(winners_list))

            if (len(numbers_have) > 0):
                result += 2 ** len(numbers_have[1:])

    return result

def part_two():
    with open("2023/day_4/input") as f:
        list_cards = []
        for line in f.read().split('\n'):
            list_cards += [line]

        cards = [1] * len(list_cards)

        for count, line in enumerate(list_cards):
            numbers = line.split("|", 1)[0].split(":", 1)[1]
            numbers_list = set(re.findall('\d+', numbers))
            winners = line.split("|", 1)[1]
            winners_list = set(re.findall('\d+', winners))

            numbers_have = list(numbers_list.intersection(winners_list))

            matching_numbers = len(numbers_have)

            for i in range(matching_numbers):
                cards[count+1+i] += cards[count]

        return sum(cards)

print(part_one())
print(part_two())
