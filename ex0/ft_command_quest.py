#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_command_quest.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/25 14:00:31 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/25 14:06:58 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import sys


def main() -> None:
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
