import math

def is_square(n):
    if n < 0:
        return False
    elif n == 0:
        return True
    elif (n % math.sqrt(n)) != 0:
        return False
    else:
        return True