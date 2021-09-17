def square(a):
    return a*a

def cube(a):
    return a*a*a

func = [square, cube]
for i in range(6):
    value = list(map(lambda x:x(i), func))
    print(value)