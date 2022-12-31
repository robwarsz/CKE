import math

with open ("liczby.txt") as file:
    lines = file.read().split('\n')
file.close()
numbers = [int(el) for el in lines]
# print(numbers)

N=100

def pierwsza(x):
    for el in range(2,int(math.sqrt(x))+1):
        if x%el==0:
            return False
    return True

# zad 3.2    *****************************************************************************************
odp1=0
for el in numbers:
    if pierwsza(el-1):
        odp1+=1
print(f'Odp 3.2: {odp1}')

#zad 3.3    *****************************************************************************************
NP=1000001
sito=[0]*NP
for el in range(2,int(math.sqrt(NP))+1):
    q = el*2
    if sito[el] == 0:
        while q <= NP-1:
            sito[q] = 1
            q += el
# LiczbyPierwsze = []
# for el in range(2,NP):
#     if sito[el] == 0:
#         LiczbyPierwsze.append(el)
# print(LiczbyPierwsze)

def para(x):
    global wyniki
    wyniki[x] = 0
    for el in range( 2 , x//2+1 ):
        if sito[el]==0:
            sec = x - el
            if el+sec == x and sito[sec] == 0:
                # print(el,sec)
                wyniki[x] += 1

wyniki={}
for number in numbers:
    para(number)
wyniki = sorted((value,key) for (key,value) in wyniki.items())
# print(wyniki)
print('Odp 3.3')
print(f'max: Liczba: {wyniki[len(wyniki)-1][1]}, ilość: {wyniki[len(wyniki)-1][0]}')
print(f'min: Liczba: {wyniki[0][1]}, ilość: {wyniki[0][0]}')


with open ("wynikiRW.txt",'w',encoding='utf8') as file:
    file.write(f'Odp 3.2: {odp1}')
    file.write('\nOdp 3.3')
    file.write(f'\nmax: Liczba: {wyniki[len(wyniki)-1][1]}, ilość: {wyniki[len(wyniki)-1][0]}')
    file.write(f'\nmin: Liczba: {wyniki[0][1]}, ilość: {wyniki[0][0]}')
file.close()

