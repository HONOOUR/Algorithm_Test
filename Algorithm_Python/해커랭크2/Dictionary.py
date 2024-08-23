from collections import Counter
# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
def sherlockAndAnagrams(s):
    string_length = len(s)
    string_arr = []
    # substring -> len(s)-1개 뽑기
    for sub_length in range(1, string_length):
        # starting index [0, 1, 2, 3] [0, 1, 2] [0, 1] [0]
        for start_index in range(string_length-sub_length+1):
            sub_string = s[start_index:start_index+sub_length]
            sub_sorted = ''.join(sorted(sub_string))
            string_arr.append(sub_sorted)
    arr_counter = Counter(string_arr)
    total_pairs = 0
    for count in arr_counter.values():
        if count > 1:
            # combination(n,2)
            total_pairs += (count*(count-1))//2
    print(total_pairs)

sherlockAndAnagrams("cdcd")