# 단계별로 풀어보기
## 9단계 기본 수학 2

#1978
N = int(input())
num_list = input().split()
except_list = []

for i in num_list:
    i = int(i)
    if i > 2:
        for j in range(2,i):
            remainder = i%j
            if remainder == 0:
                except_list.append(i)
                break
    elif i == 1:
        except_list.append(i)
    else:
        pass

last_list = [int(k) for k in num_list if int(k) not in except_list]
print(len(last_list))

#2581
M = int(input())
N = int(input())

except_list=[]
for i in range(M,N+1):
    if i > 2:
        for j in range(2,i):
            if i%j==0:
                except_list.append(i)
                break
    elif i == 1:
        except_list.append(i)
    else:
        pass

num_list = [k for k in range(M, N + 1) if k not in except_list]

if len(num_list) == 0:
    print(-1)
else:
    print(sum(num_list))
    print(min(num_list))

#11653 소인수분해
N = int(input())

quo = 2
if N == 1:
    pass
else:
    while N > 1:
        if N % quo == 0:
            N /= quo
            print(quo)
        else:
            quo += 1

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

#3009 네 번째 점
x_list = []
y_list = []
for i in range(3):
    x, y = input().split()
    x_list.append(x)
    y_list.append(y)

for j in x_list:
    if x_list.count(j) == 1:
        X = j
        break

for k in y_list:
    if y_list.count(k) == 1:
        Y = k
        break

print(X, Y)

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
print(2*(R**2)) # 택시 기하학의 원=내가 아는 정사각형 인듯?!

#1002 터렛(두 원의 위치 관계)
import math
T = int(input())

for i in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    distance = math.sqrt((x1-x2)**2+(y1-y2)**2)
    R = r1+r2
    r = abs(r1-r2)
    if (x1,y1,r1)==(x2,y2,r2):
        print(-1)
    elif distance > R or distance < r:
        print(0)
    elif distance== R or distance == r:
        print(1)
    else:
        print(2)
