
f = [0 for x in range(100)]
f[1] = 1
f[2] = 1

def fib(n = 0):
    if f[n] >= 1 :
        return f[n]
    else :
        a = fib(n - 1)
        b = fib(n - 2)
        f[n] = int(a) + int(b)
        return f[n]

def main():
    for val in range(1,20):
        print(fib(val))

if __name__ == '__main__':
    main()
