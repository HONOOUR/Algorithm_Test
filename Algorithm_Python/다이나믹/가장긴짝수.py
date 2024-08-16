length, K = map(int ,input().split())
nums = list(map(int, input().split()))
max_count = 0 
for start in range(length):
    if nums[start] % 2 == 0:
        end = start
        try_count = 0
        while try_count < K and end < length:
            if nums[end] % 2 != 0:
                try_count+=1
            end+=1
        max_count = max(max_count, len(nums[start:end])-K+1)

print(max_count)

