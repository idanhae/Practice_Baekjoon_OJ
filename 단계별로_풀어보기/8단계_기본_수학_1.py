# 단계별로 풀어보기
## 8단계 기본 수학 1

#1712 손익분기점 -> 진짜 말그대로 수학 방정식 계산임!!
import sys
A,B,C = map(int, sys.stdin.readline().split())

if C <= B:
    print(-1)
else:
    print(A//(C-B)+1) # 방정식 정리해서 판매대수 구하기
# // -> 판매대수는 자연수여야함! (몫의 정수부분만 출력! 안그러면 소수가 나올수도 있으니까)
# +1 -> ex) A/(C-B)=2.5이면 A//(C-B)=2이지만, 이득을 보려면 3대를 팔아야하니까

# 1193 분수찾기
X = int(input())

sum = 0
cnt = 0
while sum < X:
    cnt += 1
    sum += cnt

diff = sum - X

u_list = []
d_list = []
for i in range(cnt):
    u = cnt - i
    d = i + 1
    u_list.append(u)
    d_list.append(d)

if cnt % 2 == 0:  # even num
    print('{}/{}'.format(u_list[diff], d_list[diff]))
else:  # odd num
    print('{}/{}'.format(u_list[-(diff + 1)], d_list[-(diff + 1)]))

#2869
import math
A,B,V = map(int,input().split())

D = A-B
print(math.ceil((V-A)/D)+1)

#10250 ACM 호텔
import sys
T = int(input())
for i in range(T):
    H,W,N = map(int,sys.stdin.readline().split())
    if N%H == 0: # 손님 수가 층수의 배수일 때 주의
        floor = H
        room = N // H
    else:
        floor = N%H
        room = N//H+1
    print(floor*100+room) # 따로 복잡하게 형식 지정할 필요없이 이렇게 하면 간단하게 호텔방 호수 형식으로 나타낼 수 있음

#2775 부녀회장이 될테야
T = int(input())
for i in range(T):
    k = int(input())
    n = int(input())

    apt = []
    apt.append([1,2,3,4,5,6,7,8,9,10,11,12,13,14]) # floor 0
    for floor in range(k+1): # floors range 1~k
        new_floor = []
        people = 0
        for room in range(n): # range 0~n-1
             people += apt[floor][room]
             new_floor.append(people)
        apt.append(new_floor)

    print(apt[k][n-1]) # ex) 1층 2호면 apt[1][1]을 찾아야 하니까

#2839 설탕배달
N = int(input())

sum = 0
cnt = 0
while sum <= N:
    cnt += 1
    sum = 5 * cnt

diff = N - (5 * (cnt - 1))  # diff -> 결국 5로 나눈 나머지랑 경우의 수 같음(0~4)

if diff == 0:
    print(cnt - 1)
elif diff == 1:
    if cnt - 2 < 0:
        print(-1)
    else:
        print(cnt)
elif diff == 2:
    if cnt - 3 < 0:
        print(-1)
    else:
        print(cnt + 1)
elif diff == 3:
    print(cnt)
elif diff == 4:
    if N == 4:
        print(-1)
    else:
        print(cnt + 1)

#2839 설탕배달
N = int(input())

quotient = N // 5 # 몫
remainder = N % 5 # 나머지

if remainder == 0:
    print(quotient)
elif remainder == 1:
    print(quotient+1)
elif remainder == 2:
    if quotient-2<0:
        print(-1)
    else:
        print(quotient+2)
elif remainder == 3:
    print(quotient+1)
else:
    if quotient == 0:
        print(-1)
    else:
        print(quotient+2)

#2839 설탕배달 while - else!!!
N = int(input())

quo = N//5
rem = N%5
cnt = 0 # 3kg짜리 묶음 수

while quo >= 0: # N을 5로 나눈 몫에서부터 하나씩 줄여갈거니까 몫이 0이상인 동안만!
    if rem % 3 == 0: # 이러면 보따리를 풀 필요가 없음
        cnt = rem // 3
        print (quo + cnt)
        break
    quo -= 1
    rem += 5 # quo 한 보따리를 풀면 나머지에 5kg가 더해짐
# 그래서 나머지가 3의 배수가 될 때까지 반복해서 돌고
else: # 해결이 안되는 경우면 -1
    print(-1)

#10757 큰 수 A+B -> 자릿수가 많은 숫자의 연산은 어떻게 처리해야 할까
A,B = map(int,input().split())
print(A+B)
# 파이썬은 비교적 자유롭지만 만약 다른 언어(C++ 등)라면?