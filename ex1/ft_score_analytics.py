#!/usr/bin/env python3
import sys


def main():
    print("=== Player Score Analytics ===")
    length: int = len(sys.argv)
    if length == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return ()

    print(f"Total players: {length - 1}")
    temp_list = []
    for j in range(0, length - 1):
        if (j + 1 <= length):
            temp_list.append(int(sys.argv[j + 1]))
    i: int = 0
    sum: int = 0
    while i < length - 1:
        sum = sum + temp_list[i]
        i += 1
    print(f"Total score: {sum}")
    av: float = round((sum / (length - 1)), 1)
    print(f"Average score: {av}")
    print(f"High score: {max(temp_list)}")
    print(f"Low score: {min(temp_list)}")
    print(f"Score range: {max(temp_list) - min(temp_list)}")


if __name__ == "__main__":
    main()
