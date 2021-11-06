import sys
f = [x for x in range(0,101,10)]
print(f)
f = [x + y for x in 'ABCDE' for y in '1234567']
print(f)
f = [x + y for x in range(5) for y in range(x,5)]
print(f)
f = [x ** 2 for x in range(0,101,10)]
print(f)
print(sys.getsizeof(f))
print(f)
for val in f:
    print(val)
