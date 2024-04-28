def solution(S):
    occurrences = [0] * 26

    for i in range(len(S)):
        occurrences[ord(S[i]) - ord('a')] += 1

    best_char = 'a'
    best_res = 0

    for i in range(1, 26):
        if occurrences[i] >= best_res:
            best_char = chr(ord('a') + i)
            best_res = occurrences[i]

    return best_char

solution("hello")

def tuples(s):
    s = s[2:-2].split("},{")  # ["2", "2,1", "2,1,3", "2,1,3,4"]
    nums_int = set()
    for nums_str in s:
        nums_str = nums_str.split(",")
        for num in nums_str:
            nums_int.add(int(num))

    return nums_int


tuples("{{2},{2,1},{2,1,3},{2,1,3,4}}")
