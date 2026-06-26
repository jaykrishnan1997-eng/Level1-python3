import random


def gen_player_achievements() -> None:
    Alice = ['Crafting Genius', 'World Savior', 'Master Explorer', 'Collector Supreme', 'Untouchable', 'Boss Slayer']
    Bob = ['Crafting Genius', 'Strategist', 'World Savior', 'Master Explorer', 'Unstoppable', 'Collector Supreme', 'Untouchable']
    Charlie = ['Strategist', 'Speed Runner', 'Survivor', 'Master Explorer', 'Treasure Hunter', 'First Steps', 'Collector Supreme', 'Untouchable', 'Sharp Mind']
    Dylan = ['Strategist', 'Speed Runner', 'Unstoppable', 'Untouchable', 'Boss Slayer']
    for player in (Alice, Bob, Charlie, Dylan):
        print(f"Player {player}: {{ ")
        for item in player:
            
    if __name__ == "__main__":
