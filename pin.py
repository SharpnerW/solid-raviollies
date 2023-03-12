#!/bin/python
import sys
def pin_tie(pins):
    renga=0
    pins.sort()
    for x in range(1, len(pins)):
        renga+=min(pins[x], pins[x-1])
    return renga
print(pin_tie([int(x) for x in sys.argv[1::]]))

