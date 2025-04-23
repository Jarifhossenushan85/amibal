def fibonacci_series(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

# Main program
try:
    n = int(input("Enter the number of terms for the Fibonacci series: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        fibonacci_series(n)
except ValueError:
    print("Invalid input. Please enter a valid integer.")