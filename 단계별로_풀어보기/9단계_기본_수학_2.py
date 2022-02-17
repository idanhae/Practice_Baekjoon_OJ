# 단계별로 풀어보기
## 9단계 기본 수학 2

#4153 직각삼각형
while True:
    A,B,C = map(int,input().split())
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