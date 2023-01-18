# Simplified version of a past student project:
# https://github.com/BaseCampCoding/Seth-JeremiahT

import random


#---- input_pokemon_type: take input and return player_type ----#
def input_pokemon_type():
    player_type = input(
        "Please choose from these types: Fire, Grass, Rock, Ice, Ground: "
    ).upper()

    while not is_valid_type(player_type):
        player_type = input(
            "Please choose from these types: Fire, Grass, Rock, Ice, Ground: "
        ).title()
    return player_type


#---- is_valid_type: check if type is valid for program ----#
def is_valid_type(type: str) -> bool:
    type = type.title()
    types = ["Fire", "Grass", "Rock", "Ice", "Ground"]
    if type not in types: return False
    else: return True


#---- random_pokemon_type: assign random type to enemy ----#
def random_pokemon_type():
    types = ["Fire", "Grass", "Rock", "Ice", "Ground"]
    random_type = types[random.randint(0, 4)]
    return random_type


#---- has_advantage: return true if player has advantage ----#
def has_advantage(player_type: str, enemy_type: str) -> bool:
    has_fire_advantage = (player_type == "Fire"
                          and (enemy_type == "Grass" or enemy_type == "Ice"))
    has_grass_advantage = (player_type == "Grass" and
                           (enemy_type == "Rock" or enemy_type == "Ground"))
    has_rock_advantage = (player_type == "Rock"
                          and (enemy_type == "Fire" or enemy_type == "Ice"))
    has_ice_advantage = (player_type == "Ice"
                         and (enemy_type == "Grass" or enemy_type == "Ground"))
    has_ground_advantage = (player_type == "Ground"
                            and (enemy_type == "Fire" or enemy_type == "Rock"))
    has_player_advantage = (has_fire_advantage or has_grass_advantage
                            or has_rock_advantage or has_ice_advantage
                            or has_ground_advantage)
    return has_player_advantage


#---- main ----#
if __name__ == "__main__":
    print("""Here are your choices: 
    Fire
    Grass
    Rock
    Ice
    Ground
    
    Remember:
        Fire beats grass and ice 
        Grass beats rock and ground
        Rock beats fire and ice
        Ice beats grass and ground
        Ground beats fire and rock!""")

    player_health = 100
    enemy_health = 100

    while player_health > 0 and enemy_health > 0:
        player_type = input_pokemon_type()
        enemy_type = random_pokemon_type()

        if player_type == enemy_type:
            print(f"You both chose {player_type}! It's a tie!")
        else:

            if has_advantage(player_type, enemy_type):
                print(f"The computer chose {enemy_type}! You win!")
                enemy_health -= random.randint(10, 30)
            else:
                print(f"The computer chose {enemy_type}! You lose!")
                player_health -= random.randint(10, 30)

        print(f"Player health: {player_health}")
        print(f"Computer health: {enemy_health}")

    if player_health <= 0:
        print("You were defeated by the computer!\n")
    elif enemy_health <= 0:
        print("You defeated the computer!\n")
