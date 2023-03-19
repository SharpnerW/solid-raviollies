def pins(list_of_pins):
    breakpoint()
    list_of_pins.sort()
    list_of_min_range=[]
    for _ in range(len(list_of_pins)):
        list_of_min_range.append(10000)

    list_of_min_range[1]=list_of_pins[1]-list_of_pins[0]

    for i in range(2, len(list_of_min_range)):
        list_of_min_range[i] = min(list_of_min_range[i-2], list_of_min_range[i-1]) + list_of_pins[i] - list_of_pins[i-1]
    return list_of_min_range[-1]

print(pins([1,2,4,5,45,60]))
