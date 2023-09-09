#!/usr/bin/env python3

def print_fibonacci(length):
    fibonacci_list = [0,1]
    for num in range(length - 2):
        answer = fibonacci_list[-1] + fibonacci_list[-2]
        fibonacci_list.append(answer)
    print(fibonacci_list)

print_fibonacci(9)