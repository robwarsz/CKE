with open ("pary.txt") as file:
    lines = file.read().split('\n')
file.close()
N=1000
# print(lines)
numbers=[]
for el in lines:
    pair=list(map(int,el.split()))
    # print(pair)
    numbers.append(pair)
# print(numbers)

def check(pair):
    a = pair[0]
    b = pair[1]
    # print(a,b)
    while b>a:
        b//=2
    if a==b:
        return True
    return False


for el in numbers:
    if check(el):
        print(*el)
