#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_score_analytics.py                                :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/25 14:00:15 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/25 15:09:20 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    length: int = len(sys.argv)
    if length == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return ()
    temp_list = []
    error: int = 0
    for j in range(0, length - 1):
        if (j + 1 <= length):
            try:
                temp_list.append(int(sys.argv[j + 1]))
            except Exception:
                error += 1
                print(f"Invalid parameter: '{sys.argv[j + 1]}'")
    if (error != 0):
        print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
        return ()
    print(f"Total players: {length - 1}")
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
