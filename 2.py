from out_caster import * #Using module for casting array contents, written by SharpnerW, AKA me.

# Asking user input
h, w = [int(x) for x in input("W,H>").split()]
# Generating blank output array
out_array=[]
#print(out_array)
# Populating the array
for i in range(0, h):
    out_array.append([])
#    breakpoint()
    for j in range(0, w):
        out_array[i].append((i+1)*(j+1))

cast(out_array)
