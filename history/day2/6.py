import os
import time
def main():
    res = 0
    content = '北京欢迎您'
    while res <= 20 :
        res += 1
        os.system('cls')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]

if __name__ == '__main__' :
    main()
