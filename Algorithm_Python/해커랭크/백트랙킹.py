# https://www.hackerrank.com/challenges/ctci-recursive-staircase/problem?isFullScreen=true&h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking
def stepPerms(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        steps = [0 for _ in range(n+1)]
        steps[1] = 1
        steps[2] = 2
        steps[3] = 4
        for i in range(4, n+1):
            steps[i] = steps[i-1] + steps[i-2] + steps[i-3]
        return steps[n]
    