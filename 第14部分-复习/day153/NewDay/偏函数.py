from functools import partial

def ab(a,b):
    return a+b

new_ab = partial(ab,10)

print(new_ab(9))


