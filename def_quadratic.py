import math


# x= (-b+sqrt(pow(b)-4a*c))/2*a  &  (-b-sqrt(pow(b)-4a*c))/2*a

def quadratic(a, b, c):
    x1 = (-b + math.sqrt(math.pow(b, 2)-4*a*c))/2*a
    x2 = (-b - math.sqrt(math.pow(b, 2)-4*a*c))/2*a
    return(x1, x2)
