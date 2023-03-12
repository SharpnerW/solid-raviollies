from out_caster import *

#Asking user input
w, h = [int(x) for x in input("X,Y> ").split()]

#Generating blank out array
out_array=[]

#Populating Array
for i in range(0, h):
    out_array.append([])
    for j in range(0, w):
        if i==j: out_array[i].append(1)
        elif i>j: out_array[i].append(2)
        elif i<j: out_array[i].append(0)

#Casting array
cast(out_array)
