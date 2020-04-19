list = [2,3,5,6,7,6,4,3,4,4,45,24]

n = 24

def search(lst, number):
    i = 0
    while i< len(lst):
        if list[i] == number:
            return True
        i += 1
    return False

if search(list,n):
    print("Found",n)
else:
    print("Not found",n)

