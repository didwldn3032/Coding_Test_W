## ch3. 그리디 - 숫자 카드 게임
N, M = map(int, input().split())
res = -1

for _ in range(N):
    res = max(res, min(list(map(int, input().split(sep = ' ')))))

print(res)