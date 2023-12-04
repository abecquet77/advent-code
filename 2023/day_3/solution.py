import re
from collections import defaultdict

def part_one():
    result = 0
    with open("2023/day_3/input") as f:
        matrice = []
        for line in f.read().split('\n'):
            matrice += [line]
        len_r = len(matrice)
        len_c = len(matrice[0])

        for r, row in enumerate(matrice):
            for match in re.finditer(r'\d+', row):
                number = match.group()
                part_number = False
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        for c in range(*match.span()):
                            if 0 <= (r+rr) < len_r and 0 <= (c+cc) < len_c:
                                ch = matrice[r+rr][c+cc]
                                if not ch.isdigit() and ch != '.':
                                    part_number = True
                if (part_number):
                    result += int(number)

        return result

def part_two():
    result = 0
    with open("2023/day_3/input") as f:
        matrice = []
        for line in f.read().split('\n'):
            matrice += [line]
        len_r = len(matrice)
        len_c = len(matrice[0])

        multi = defaultdict(list)

        for r, row in enumerate(matrice):
            for match in re.finditer(r'\d+', row):
                number = match.group()
                part_number = False
                for rr in [-1, 0, 1]:
                    for cc in [-1, 0, 1]:
                        for c in range(*match.span()):
                            if 0 <= (r+rr) < len_r and 0 <= (c+cc) < len_c:
                                ch = matrice[r+rr][c+cc]
                                if ch == '*':
                                    part_number = True
                                    asterix = str(r+rr)+str(c+cc)

                if (part_number):
                    multi[asterix].append(number)
                    if (len(multi[asterix]) == 2):
                        gear = int(multi[asterix][0])*int(multi[asterix][1])
                        result += gear

        return result

print(part_one())
print(part_two())
