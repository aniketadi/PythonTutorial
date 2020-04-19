def div(a,b):
    print(a/b)


def smartDiv(funcAsParameter):
    def inner(a,b):
        if a<b:
            a,b = b,a
        return funcAsParameter(a,b)
    return inner


div = smartDiv(div)
div(2,4)