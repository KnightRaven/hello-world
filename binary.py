def binary(i, figure, upper, lower):
    middle = search(upper, lower)
    i+=1
    if middle == figure:
        return i
    elif middle>hit:
        return binary(i, figure, middle, lower)
    elif middle<hit:
        return binary(i, figure, upper, middle)

def search(upper, lower):
    middle=int((upper+lower)/2)
    return middle

if __name__=='main':
    print binary(0, 3, 100, 0)
