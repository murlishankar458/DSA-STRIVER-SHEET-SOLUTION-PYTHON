n = int(input())
def numFactorial(n):
    if n == 0:
        return 1
    return n* numFactorial(n-1)
