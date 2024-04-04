import random


def open_file():
    random_number = random.randint(1, 5)
    with open(f"input{str(random_number)}.txt", "r") as file:
        i, j = map(int, file.readline().split())
        return i, j


def main():
    i, j = open_file()
    Max = [0] * (j - i + 1)

    for a in range(i, j + 1):
        b = 1
        c = a
        while c != 1:
            if c % 2 == 0:
                c //= 2
            else:
                c = c * 3 + 1
            b += 1
        Max[a - i] = b
    print(i, j, max(Max))


if __name__ == "__main__":
    main()
