import mymod

def main():
    print("최상위 모듈시, 출력됩니다")


def power(x, y):
    r = 1
    for i in range(y):
        r = mymod.multiply(r, x)
    return r


if __name__ == '__main__':
    main()
else:
    print('모듈이름:' + __name__)