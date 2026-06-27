#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_data_stream.py                                    :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: jkrishna <jkrishna@student.42.fr>            +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/06/27 14:13:29 by jkrishna            #+#    #+#            #
#   Updated: 2026/06/27 16:36:47 by jkrishna           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


import typing
import random


def gen_event() -> typing.Generator[tuple[str, str], None, None]:
    actions = [
        'run', 'eat', 'sleep', 'grab', 'move', 'climb',
        'swim', 'release'
    ]
    names = ['alice', 'bob', 'dylan', 'charlie']
    while True:

        yield (random.choice(names), random.choice(actions))


def consume_event(
    event_list: list[tuple[str, str]]
) -> typing.Generator[tuple[str, str], None, None]:
    while len(event_list) > 0:
        event = random.choice(event_list)
        print(f"Got event from list: {event}")
        event_list.remove(event)
        print(f"Remains in list: {event_list}")
        yield (event)


if __name__ == "__main__":
    gen = gen_event()
    for i in range(0, 1000):
        event_gen = next(gen)
        # print(f"Event {i}: Player {event_gen[0]} did action {event_gen[1]}")
    event_list = [next(gen) for _ in range(10)]
    print(f"Built list of 10 events: {event_list}")
    for event in consume_event(event_list):
        pass
