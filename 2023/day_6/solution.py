import re
import time

races={}

def part_one():
    with open("2023/day_6/input") as f:
        first_line = f.readline().strip('\n')
        
        races_time = re.findall('\d+', first_line)

        second_line = f.readline().strip('\n')

        races_distance = re.findall('\d+', second_line)

        races = dict(zip(races_time, races_distance))

        ways=1

        for j in races:
            results={}
            race_total_duration=int(j)
            record=int(races[j])

            for hold_duration in range(1,race_total_duration+1):
                speed=hold_duration
                race_duration=race_total_duration-hold_duration
                distance=speed*race_duration
                if(distance>record):
                    results[hold_duration]=distance

            ways=ways*len(results)

    return ways

def part_two():
    with open("2023/day_6/input") as f:
        first_line = f.readline().strip('\n')
        
        races_time = ''.join(re.findall('\d+', first_line))

        second_line = f.readline().strip('\n')

        races_distance = ''.join(re.findall('\d+', second_line))

        races = {races_time: races_distance}

        ways=1

        for j in races:
            results={}
            race_total_duration=int(j)
            record=int(races[j])

            for hold_duration in range(1,race_total_duration+1):
                speed=hold_duration
                race_duration=race_total_duration-hold_duration
                distance=speed*race_duration
                if(distance>record):
                    results[hold_duration]=distance

            ways=ways*len(results)

    return ways

start = time.time()
print(f'Result part one : {part_one()}')
end = time.time()
print(f'Part one duration : {end - start} seconds')
start = time.time()
print(f'Result part two : {part_two()}')
end = time.time()
print(f'Part two duration : {end - start} seconds')