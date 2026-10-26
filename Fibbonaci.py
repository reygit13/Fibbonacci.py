
def fibonacci(n):
    a, b = 0, 1

    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b


def main():
    n = int(input("Enter the number of terms: "))

    if n > 0:
        fibonacci(n)
    else:
        print("Enter a positive number.")


if __name__ == "__main__":
    main()
