#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_achievement_tracker.py                            :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/27 11:21:09 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/27 12:08:06 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

import random


def gen_player_achievements() -> set[str]:
    achievements = [
        'Crafting Genius', 'World Savior', 'Master Explorer',
        'Collector Supreme', 'Untouchable', 'Boss Slayer',
        'Strategist', 'Speed Runner', 'Survivor',
        'Treasure Hunter', 'First Steps', 'Hidden Path Finder',
        'Unstoppable', 'Sharp Mind'
    ]
    count = random.randint(1, len(achievements))
    collect = random.sample(achievements, count)
    return set(collect)


if __name__ == "__main__":
    print("=== Achievement Tracker System ===\n")
    names = ["Alice", "Bob", "Charlie", "Dylan"]
    sets = [gen_player_achievements() for _ in names]
    for i in range(len(names)):
        print(f"Player {names[i]}: {sets[i]}")
    all_achievement = set.union(*sets)
    print(f"All distinct achievements: {all_achievement}\n")
    common_achievement = set.intersection(*sets)
    print(f"Common achievements: {common_achievement}\n")
    for i in range(len(names)):
        others = [sets[j] for j in range(len(names)) if j != i]
        others_union = set.union(*others)
        diff = sets[i].difference(others_union)
        print(f"Only {names[i]} has: {diff}")
    print("\n")
    for j in range(len(names)):
        missing = all_achievement.difference(sets[j])
        print(f"{names[j]} is missing: {missing}")
