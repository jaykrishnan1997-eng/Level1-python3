#!/usr/bin/env python3
import sys


def main():
    print("=== Command Quest ===")
    print(f"Program name: {sys.argv[0]}")
    length: int = len(sys.argv)
    if length == 1:
        print("No arguments provided!")
    else:
        print(f"Arguments recieved: {length - 1}")
        i: int = 1
        while i < length:
            print(f"Argument {i}: {sys.argv[i]}")
            i += 1
    print(f"Total arguments: {length}")


if __name__ == "__main__":
    main()
