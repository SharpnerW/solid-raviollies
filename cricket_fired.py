#!/bin/python

def count_jumps(N, stones):
    steps=[1,1]
    for j in range(2, N+1):
        steps.append((j not in stones)*(steps[j-2]+steps[j-1]))
    return steps[-1]
print(count_jumps(, [3, 5]))
