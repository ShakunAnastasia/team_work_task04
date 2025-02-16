def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

def tobase(n, base):
    new = 0
    place = 1
    while n > 0:
        new += (n % base) * place
        n //= base
        place *= 10
    return new
