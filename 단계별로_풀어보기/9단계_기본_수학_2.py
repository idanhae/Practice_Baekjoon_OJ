# 단계별로 풀어보기
## 9단계 기본 수학 2

#1085 직사각형에서 탈출
x, y, w, h = map(int,input().split())
hw = w/2
hh = h/2

if x<=hw and y<=hh:
    print(min(x,y))
elif x<=hw and y>=hh:
    print(min(x,h-y))
elif x>=hw and y<=hh:
    print(min(w-x,y))
elif x>=hw and y>=hh:
    print(min(w-x,h-y))

#4153 직각삼각형
while True:
    A,B,C = map(int, input().split())
    if A==B==C==0:
        break
    else:
        if A**2+B**2 == C**2:
            print('right')
        elif C**2+B**2 == A**2:
            print('right')
        elif A**2+C**2 == B**2:
            print('right')
        else:
            print('wrong')

#3053 택시 기하학
import math
R = int(input())
print(math.pi*(R**2))
print(2*(R**2)) # 택시 기하학의 원=내가 아는 마름모 인듯?!