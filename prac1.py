import random
random_number = random.randint(1,100)
a = 0
n = 1

print('1부터 100 사이의 숫자릅 입력해주세요.')
while not a == random_number:
    a = int(input())
    if a < random_number:
        print('UP')
        n += 1
    elif a > random_number:
        print('DOWN')
        n += 1
    else:
        print('정답!')
        print('시도 횟수:')
        print(n)