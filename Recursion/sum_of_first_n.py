n = int(input())
def sumNumbers(n):
    if n == 0:
        return 0
    return n +sumNumbers(n-1)
print(sumNumbers(n))
