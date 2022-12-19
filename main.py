def progression(n, start=5, d=3):
    if n <= 0:
        raise ValueError
    return start + (n - 1) * d


if __name__ == "__main__":
    print("Мєзєнцев Єгор Миколайович")

    n = int(input("Введіть номер n-того елементу: "))

    print(progression(n))