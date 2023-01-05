#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv, exit


def main():
    arguments = argv[1:]
    if len(arguments) != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    operators = ['+', '-', '*', '/']
    functions = [add, sub, mul, div]

    if arguments[1] not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(arguments[0])
    b = int(arguments[2])

    for index, operator in enumerate(operators):
        if arguments[1] != operator:
            continue
        result = functions[index](a, b)
        print(f"{a:d} {operator:s} {b:d} = {result:d}")


if __name__ == "__main__":
    main()
