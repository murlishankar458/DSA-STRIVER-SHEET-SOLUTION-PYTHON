n = int(input())

def printNumbers(i):
    if i>n:
        return
    print(i)
    printNumbers(i+1)
printNumbers(1)
