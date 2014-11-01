__author__ = 'jianxinsun'


def check_pythagorean(a, b, c):
    return a ** 2 + b ** 2 == c ** 2


def search_pythagorean(max_number=1000):
    for a in range(max_number / 3):
        for b in range(a + 1, (max_number - a) / 2):
            c = max_number - a - b
            if check_pythagorean(a, b, c):
                print a, b, c
                print a * b * c
                return


def main():
    search_pythagorean(1000)


if __name__ == "__main__":
    main()