W = input('Please enter a string :\t')
def most_frequent(string):
    d = dict()
    for key in string:
        if key not in d:
            d[key] = 1
        else:
            d[key] += 1
    return d
a=most_frequent (reversed ("Mississippi"))
print(a)
