from functools import partial

def ab(a,b):
    print(a)
    return a+b

new_ab = partial(ab,"request")

print(new_ab("200 OK!"))