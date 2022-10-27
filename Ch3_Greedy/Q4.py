## ch3. 그리디 - 1이 될 때까지
N, K = map(int, input().split())

res = 0

while N % K != 0:
    N -= 1
    res += 1

while N != 1:
    N /= K
    res += 1

print(res)