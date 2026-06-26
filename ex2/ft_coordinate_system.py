#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_coordinate_system.py                              :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/26 15:56:07 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/26 17:27:13 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import math


def get_player_pos() -> tuple:
    i: int = 0
    check: int = 0
    while (check == 0):
        try:
            coords = []
            string = input("Enter new cordinates as floats in format 'x,y,z': ")
            parts = string.split(",")
            if len(parts) != 3:
                raise IndexError("Invalid syntax")
            for part in parts:
                coords.append(float(part))
            X = tuple(coords)
            check = 1
        except IndexError as e1:
            print(f"{e1}")
        except ValueError as e:
            print(f"Error on parameter '{part}': {e}")
    return (X)


if __name__ == "__main__":
    print("Get a first set of coordinates")
    X = get_player_pos()
    print(f"Got a first tuple: ({X[0]}, {X[1]}, {X[2]})")
    print(f"It includes: X={X[0]}, Y={X[1]}, Z={X[2]}")
    print("Distance to center: " + str(round(math.sqrt(X[0]**2 + X[1]**2 + X[2]**2), 4)) + "\n")
    
    print("Get a second set of coordinates")
    Y = get_player_pos()
    print("Distance between the 2 sets of coordinates: " + str(round(math.sqrt((Y[0] - X[0])**2 + (Y[1] - X[1])**2 + (Y[2] - X[2])**2), 4)))
