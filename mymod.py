def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    return a / b


def main():
    print("최상위 모듈시, 출력됩니다")


if __name__ == '__main__':
    main()
else:
    print('모듈이름:' + __name__)


