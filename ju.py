def lst(a):
    for i in range(a):
        yield(i**i)

for i in lst(10):
    print(i)
