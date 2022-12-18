def progression(start, d, n):
    if n < 0:
        raise ValueError
    return (n / 2) * (2 * start + (n - 1) * d)


if __name__ == "__main__":
    print("Мєзєнцев Єгор Миколайович")

    n = int(input("Введите кол-во: "))
    d = int(input("Введите розность: "))
    start = int(input("Введите начальное значение: "))

    print(progression(start, d, n))