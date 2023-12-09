def next_line(numbers):
    next=[]
    for current, next_number in zip(numbers, numbers[1:]):
        diff = int(next_number) - int(current)
        next.append(diff)
    return next

def part_one():
    with open("2023/day_9/input") as f:
        lignes = f.readlines()
        result=0
        for ligne in lignes:
            #print(ligne)
            numbers = list(map(int, ligne.split()))
            #print(numbers)
            predictions=[]
            while(True):
                predictions.append(numbers)
                numbers=next_line(numbers)
                if all(i == 0 for i in numbers):
                    predictions.append(numbers)
                    break
            predictions=list(reversed(predictions))
            for i,line in enumerate(predictions):
                if all(value == 0 for value in line):
                    line.append(0)
                else:
                    new=predictions[i][-1]+predictions[i-1][-1]
                    line.append(new)
                #print (line)
            result+=predictions[-1][-1]
        #print(result)
    return result

def part_two():
    with open("2023/day_9/input") as f:
        lignes = f.readlines()
        result=0
        for ligne in lignes:
            #print(ligne)
            numbers = list(map(int, ligne.split()))
            #print(numbers)
            predictions=[]
            while(True):
                predictions.append(numbers)
                numbers=next_line(numbers)
                if all(i == 0 for i in numbers):
                    predictions.append(numbers)
                    break
            predictions=list(reversed(predictions))
            for i,line in enumerate(predictions):
                if all(value == 0 for value in line):
                    line.insert(0,0)
                else:
                    new=predictions[i][0]-predictions[i-1][0]
                    line.insert(0,new)
                #print (line)
            result+=predictions[-1][0]
        #print(result)
    return result

print(part_one())
print(part_two())

        
        

