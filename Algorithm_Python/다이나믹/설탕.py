N = int(input())

bags = [-1 for _ in range(N+1)]
bags[3] = 1
bags[5] = 1
for i in range(4, N+1):
  if i % 5 == 0:
    bags[i] = bags[i-5]+1
  elif i % 3 == 0:
    bags[i] = bags[i-3]+1
  else:
    bags[i] = bags[i-1]
    
print(bags[N])