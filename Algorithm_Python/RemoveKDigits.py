# https://leetcode.com/problems/remove-k-digits/
# - remove k digits
# - 앞에서부터 뒤에 수가 더 작으면 앞을 지운다

#     if nums[i] > nums[i+1]

# - k 개 지웠을 때, i 가 배열을 넘어가지 않을 때까지 반복한다.
# - 조건
#     1. if nums[i] > nums[i+1] → remove nums[i] and count k up
#     2. 포인터 i 가 index 밖으로 넘어가지 않도록 i==0 이면 i 를 그대로 두고, nums[i] > nums[i+1] i -= 1 하고 그 이 외의 경우 i += 1
#     3. 예외처리를 해준다 한자리일 경우(len(nums) == 0) 포함 더 k만큼 못지웠을 때, 앞자리가 0 일때

def removeKdigits(self, num: str, k: int) -> str:
    nums = []
    for n in num:
        nums.append(int(n))
    answer = ""
    removed_count = 0
    i = 0
    # 8 9 0  1 4 3 2 2 1
    while removed_count != k and i > -1 and i < len(nums)-1:
        if i == 0 and nums[0] > nums[1]:
            nums.pop(0)
            removed_count += 1
        elif nums[i] > nums[i+1]:
            nums.pop(i)
            removed_count += 1
            i -= 1
        else:
            i += 1
    while removed_count < k:
        nums.pop()
        removed_count += 1

    while len(nums) > 0 and nums[0] == 0:
        nums.pop(0)
    for num in nums:
        answer += str(num)

    if answer == "":
        answer = "0"

    return answer


def removeKdigits_stack(self, num: str, k: int) -> str:
    stack_num = []
    for n in num:
        temp = int(n)
        # if len(stack_num) > 0:
        while len(stack_num) > 0 and stack_num[len(stack_num)-1] > temp and k > 0:
            stack_num.pop()
            k -= 1

        if len(stack_num) == 0 and temp == 0:
            continue
        else:
            stack_num.append(temp)

    while k > 0 and len(stack_num) > 0:
        stack_num.pop()
        k -= 1

    answer = ""
    for num in stack_num:
        answer += str(num)
    if answer == "":
        answer = "0"

    return answer


num = "1432219"
k = 3

removeKdigits(num, k)
removeKdigits_stack(num, k)
