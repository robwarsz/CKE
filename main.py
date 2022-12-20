''' 22:20 '''

# f = open("mecz_przyklad.txt", "r")
# points=f.read()
# # print(type(points))
# print(points)

points=[]
# with open("mecz_przyklad.txt", "r") as file:
with open("mecz.txt", "r") as file:
    for line in file:
        for char in line:
            points.append((char))
# print(points)
# print(len(points))

def part1():
    global points
    result=0
    last=points[0]
    for point in points:
        if point != last:
            last = point
            result += 1
    return f'Odp1: {result}'

def part2():
    scoreA=0
    scoreB=0
    global points
    for point in points:
        if point == 'A':
            scoreA += 1
        else:
            scoreB += 1
        if scoreA >= 1000 and abs(scoreA-scoreB)>2 or scoreB >= 1000 and abs(scoreA-scoreB)>2:
            return f'\nOdp2: Zwycięzca: {"A" if scoreA > scoreB else "B"}, Wynik: {scoreA}:{scoreB}'

def part3():
    scoreA=[0]*10000
    scoreB=[0]*10000
    A10=0
    B10=0
    global points
    if points[0] == 'A':
        scoreA[0] = 1
    else:
        scoreB[0] = 1
    for el in range(1,10000):
        if points[el]=='A':
            scoreA[el] = scoreA[el-1]+1
            scoreB[el] = 0
        else:
            scoreB[el] = scoreB[el-1]+1
            scoreA[el] = 0
        if scoreA[el] == 10:
            A10 += 1
        if scoreB[el] == 10:
            B10 += 1
    maxA=max(scoreA)
    maxB=max(scoreB)
    # return [maxA,maxB,A10,B10]
    return f'\nOdp3: Najdłuższa passa: {"A" if maxA > maxB else "B"}, długość passy: {max(maxA,maxB)}, Ilośc dobrych pass: {A10+B10}'

with open ("wynikiRW-PY.txt","w",encoding='utf-8') as file:
    file.write(part1())
    file.write(part2())
    file.write(part3())
file.close()


print(part1())
print(part2())
print(part3())

