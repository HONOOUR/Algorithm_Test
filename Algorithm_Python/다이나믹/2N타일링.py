N = int(input())

tile = [0 for _ in range(N+1)]
tile[1] = 1
tile[2] = 2
for i in range(3, N+1):
    tile[i] = tile[i-1]+tile[i-2]

print(tile[N]%10007)