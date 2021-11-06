import time
def main():
    with open('2.txt','r',encoding = 'UTF-8') as f:
        print(f.read())

    with open('2.txt',mode = 'r') as f:
        for line in f:
            print(line,end = ' ')
            time.sleep(2)
    print()

    with open('2.txt') as f:
        lines = f.readlines()
    print(lines)

if __name__ == '__main__':
    main()
