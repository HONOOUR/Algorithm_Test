# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumBribes(q):
    for i in range(len(q)-1, -1, -1):
        if i+1 < q[i]-2:
            print('Too chaotic')
            return
    bribe_count = 0
    for i in range(len(q)): # to i 
        for j in range(max(0, q[i]-2), i): # count bigger number before i
            if q[i] < q[j]:
                bribe_count += 1
    print(bribe_count)


def minimumSwaps(arr):
    count = 0
    for i in range(len(arr)):
        # Skip if the element is already in the correct position
        while arr[i] != i + 1:
            # Find the index where the current element should be
            correct_index = arr[i] - 1
            
            # Swap the element to its correct position
            temp = arr[i]
            arr[i] = arr[correct_index]
            arr[correct_index] = temp
            
            # Increase the swap count
            count += 1

    return count

from collections import Counter
def twoStrings(s1, s2):
    # substring length >= 1
    if (Counter(s1) - Counter(s2)) != Counter(s1):
        return 'YES'
    else:
        return 'NO'
    
def twoStrings_faster(s1, s2):
    if set(s1) & set(s2):
        return 'YES'
    else:
        return 'NO'