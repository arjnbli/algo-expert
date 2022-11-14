# O(n) time | O(n) space 
# n is the length of the input array
def hasSingleCycle1(array):
    # Write your code here.
    visited = [False for jump in array]
    idx = 0
    numJumps = 0
    while numJumps < len(array):
        idx = (idx + array[idx]) % len(array)
        visited[idx] = True
        numJumps += 1
    for isVisited in visited:
        if isVisited is False:
            return False
    return True

# O(n) time | O(1) space 
# n is the length of the input array
def hasSingleCycle2(array):
    # Write your code here.
    idx = 0
    num_jumps = 0
    while num_jumps < len(array):
        if num_jumps != 0 and idx == 0:
            return False
        idx = (idx + array[idx]) % len(array)
        num_jumps += 1
    return idx == 0
