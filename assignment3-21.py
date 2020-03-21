import math
def quadratic(a, b, c):
    if b*b >= 4*a*c:
        x1 = (-b+math.sqrt(b*b-4*a*c))/(2*a)
        x2 = (-b-math.sqrt(b*b-4*a*c))/(2*a)
        return x1, x2
    else:
        return None

# for test purpose
x1, x2 = quadratic(1, 3, 2)
print(x1, x2)


    