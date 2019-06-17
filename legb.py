
# LEGB 규칙
# 1. Local
# 2. Enclosing Function(내포한 함수)
# 3. Global
# 4. Built-in

a = 1 # G


def f():
    b = 200 # E

    def g():
        b = 100 # L
        print(b)
        print(__name__)
    g()


if __name__ == '__main__':
    f()

