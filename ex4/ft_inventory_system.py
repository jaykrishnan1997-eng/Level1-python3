#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_inventory_system.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/27 12:33:56 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/27 14:11:32 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import sys


if __name__ == "__main__":
    print("=== Inventory System Analysis ===")
    len: int = len(sys.argv)
    # item_list = ['sword', 'potion', 'shield', 'armor', 'helmet']
    tot_value: int = 0
    key_count: int = 0
    max_value = float('-inf')
    min_value = float('inf')
    Dictionary = {}
    for i in range(1, len):
        if ":" not in sys.argv[i]:
            print(f"Error - invalid parameter '{sys.argv[i]}'")
            continue
        key, value = sys.argv[i].split(":")
        if key in Dictionary:
            print(f"Redundant item '{key}' - discarding")
            continue
        try:
            Dictionary[key] = int(value)
            tot_value += int(value)
            key_count += 1
        except ValueError as e:
            print(f"Quantity error for '{key}': " + str(e))
    print(f"Got inventory: {Dictionary}")
    print(f"Item list: {list(Dictionary.keys())}")
    print(f"Total quantity of the {key_count} items: {tot_value}")
    for key in Dictionary:
        percent = round(float(Dictionary[key] / tot_value) * 100, 1)
        print(f"Item {key} represents {percent}%")
    for key in Dictionary:
        if (Dictionary[key] > max_value):
            max_key = key
            max_value = Dictionary[key]
    print(f"Item most abundant: {max_key} with quantity {max_value}")
    for key in Dictionary:
        if (Dictionary[key] < min_value):
            min_key = key
            min_value = Dictionary[key]
    print(f"Item least abundant: {min_key} with quantity {min_value}")
    Dictionary.update({"magic_item": 1})
    print(f"Updated inventory: {Dictionary}")
