# def highest_even(li):
#    max = 0
#    for item in li:
#        if item % 2 == 0:
#            if item > max:
#                max = item
#    return max


def highest_even(li):
    evens = []
    for item in li:
        if item % 2 == 0:
            evens.append(item)
    return max(evens)


print(highest_even([2, 3, 4, 8, 10, 11]))
