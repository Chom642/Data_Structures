def fibonacci():
    num = int(input("Enter sequence length: "))
    if num < 0:
        print("Enter a number greater than 0")
    else:
        for n in range(num):
            print(print_fib(n))

def print_fib(i):
    if i <= 1:
        return i
    else:
        return(print_fib(i-2) + print_fib(i-1))