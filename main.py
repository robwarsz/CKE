# f = open("mecz_przyklad.txt", "r")
# points=f.read()
# # print(type(points))
# print(points)

points=[]
with open("mecz_przyklad.txt", "r") as file:
    for line in file:
        for char in line:
            points.append((char))
# print(points)

def part1():
    global points
    result=0
    last=points[0]
    for point in points:
        if point != last:
            last = point
            result += 1
    return result

print(f'{part1()}')