## ch3. 그리디 - 큰 수의 법칙
N, M, K = map(int, input().split())
arr = list(map(int, input().split()))

## 가장 큰수
max_num = max(arr)
arr.remove(max_num)

## 두번째로 큰수
second = max(arr)

res = 0
flag = K

for _ in range(M):
    if flag == 0:
        res += second  
        flag = K
    else:
        res += max_num
        flag -= 1

print(res)