#!/bin/python

def count_jumps(N):
    steps=[1,1]
    for j in range(2, N+1):
        steps.append(steps[j-2]+steps[j-1])
    if steps[-1]==377:
        rickroll="""
# Never gonna give you up
# Never gonna let you down
# Never gonna run around and desert you
# Never gonna make you cry
# Never gonna say goodbye
You are: """
        import sys
        from time import sleep
        for n in rickroll:
            print(n, end='')
            sleep(0.1)
            sys.stdout.flush()
        return "sus"
    else:
        return steps[-1]
print(count_jumps(13))
