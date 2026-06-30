#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_alchemist.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/30 12:27:32 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/30 14:14:43 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import random


if __name__ == "__main__":
    count: float = 0
    sum: float = 0
    initial_player_list = ['Alice', 'bob', 'Charlie', 'dylan', 'Emma', 'Gregory', 'john', 'kevin', 'Liam']
    print(f"Initial list of players: {initial_player_list}")
    new_player_list = [i.capitalize() for i in initial_player_list]
    print(f"New list with all names capitalized: {new_player_list}")
    cap_only_list = [i for i in initial_player_list if i == i.capitalize()]
    print(f"New list of capitalized names only: {cap_only_list}")
    score_dict = {i: random.choice(range(1, 1000)) for i in initial_player_list}
    print(f"Score_dict: {score_dict}")
    for key in score_dict.keys():
        count += 1
        sum = sum + float(score_dict[key])
    average: float = sum / count
    print(f"Score average is {round(average, 2)}")
    high_score_dict = {key: score_dict[key] for key in score_dict.keys() if float(score_dict[key]) > average}
    print(f"High scores: {high_score_dict}")
