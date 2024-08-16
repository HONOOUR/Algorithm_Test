# https://www.hackerrank.com/challenges/new-year-chaos/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays
def minimumBribes(q):
    # more than 2 
    for i in range(len(q)-1, -1, -1):
        if i+1 < q[i]-2:
            print('Too chaotic')
            return
    # bribe count
    bribe_count = 0
    for i in range(len(q)):
        for j in range(max(0, q[i]-2), i):
            if q[i] < q[j]:
                temp = q[i]
                q[i] = q[j]
                q[j] = temp
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
