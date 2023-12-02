import re

color_patterns = {
    'blue': '(\d+)\s+blue',
    'red': '(\d+)\s+red',
    'green': '(\d+)\s+green',
}

def part_one():
    possible = {
        'red' : 12 ,
        'green' : 13,
        'blue' : 14
    } 

    result=0

    with open("2023/day_2/input") as f:
        for line in f.read().split('\n'):
            game_possible = True
            game_id=int(re.search('\d+',line.split(":",1)[0]).group())
            cubes=line.split(":",1)[1]

            for color, pattern in color_patterns.items():
                for match in re.finditer(pattern,cubes):
                    number=int(match.group(1))
                    if int(number) > possible[color]:
                        game_possible = False
                        break

            if game_possible:
                #print(f"Game {game_id} OK")
                result+=int(game_id)

    return result

def part_two():

    result=0

    with open("2023/day_2/input") as f:
        for line in f.read().split('\n'):
            cubes=line.split(":",1)[1]

            color_number_max = {'blue': 0, 'red': 0, 'green': 0}

            for color, pattern in color_patterns.items():
                for match in re.finditer(pattern,cubes):
                    number=int(match.group(1))
                    color_number_max[color]=max(number,color_number_max[color])

            power=color_number_max['blue']*color_number_max['green']*color_number_max['red']

            result+=power

    return result

print(part_one())
print(part_two())
