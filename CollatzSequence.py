print("Varun Bellad, 1AY24AI096, Sec-O")
# CollatzSequence.py

def collatz(number):
    if number % 2 == 0:
        return number // 2
    else:
        return 3 * number + 1

def main():
    try:
        n = int(input("Enter a positive integer: "))
        if n <= 0:
            print("Please enter a number greater than 0.")
            return

        print(f"Collatz sequence starting from {n}:")
        while n != 1:
            print(n, end=' -> ')
            n = collatz(n)
        print(1)  # End of the sequence

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
