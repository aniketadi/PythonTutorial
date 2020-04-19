
def recursionWithoutLoop(n):
    print(n)
    n += 1
    if n <=200:
        recursionWithoutLoop(n)

recursionWithoutLoop(1)
