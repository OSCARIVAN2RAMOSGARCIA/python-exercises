import time
import numpy as np
import sys
import pandas as pd

#print a letter with delay 
def print_with_delay(s):
    # Function to print each character of a string with a delay
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

#create a pokemon class
class Pokemon:
    def __init__(self, name, type, moves, evolutions, points_of_health='================'):
        # Constructor to initialize attributes of the Pokemon class
        self.name = name
        self.type = type
        self.moves = moves
        self.attack = evolutions['attack']
        self.defense = evolutions['defense']
        self.points_of_health = points_of_health
        self.bar = 20 # amount of health points
    
    def print_Info(self, pokemon2):
        # Method to print battle information
        print("--------Battle Pokemon--------")
        print(f"\n{self.name}")
        print("type/", self.type)
        print("attack/", self.attack)
        print("defense/", self.defense)
        print("Nv./", 3*(1+np.mean([self.attack, self.defense])))
        print("\nVS")
        print(f"\n{pokemon2.name}")
        print("type/", pokemon2.type)
        print("attack/", pokemon2.attack)
        print("defense/", pokemon2.defense)
        print("Nv./", 3*(1+np.mean([pokemon2.attack, pokemon2.defense])))
        time.sleep(2)
        
    def advantage(self, pokemon2):
        # Method to determine the advantage of one Pokemon over another based on type
        version = ['fire','water','grass','electric']
        
        for i, k in enumerate(version):
            if self.type == k:
                # they are the SAME type
                if pokemon2.type == k:
                    string_1_attack = "\nIt isn't very effective..."
                    string_2_attack = "\nIt isn't very effective..."
                # pokemon2 is STRONG
                if pokemon2.type == version[(i+1)%3]:
                    pokemon2.attack *= 2
                    pokemon2.defense *= 2
                    self.attack /= 2
                    self.defense /= 2

                    string_1_attack = "\nIt isn't very effective..."
                    string_2_attack = "\nIt's very effective..."

                # pokemon2 is WEAK
                if pokemon2.type == version[(i+2)%3]:
                    self.attack *= 2
                    self.defense *= 2
                    pokemon2.attack /= 2
                    pokemon2.defense /= 2

                    string_1_attack = "\nIt is very effective..."
                    string_2_attack = "\nIt isn't very effective..."
        return string_1_attack, string_2_attack
    
    def turn(self, pokemon2, string_1_attack, string_2_attack):
        # Method to simulate a turn in the battle between two Pokemon
        while self.bar > 0 and pokemon2.bar > 0:
            # Print the health points of each Pokémon
            print(f"\n{self.name}\t\tPS\t{self.points_of_health}") 
            print(f"{pokemon2.name}\t\tPS\t{pokemon2.points_of_health}") 

            print(f"GO {self.name}!")

            for i, x in enumerate(self.moves):
                print(f"{i+1}.", x)
            index = int(input("Choose a move: "))
            print_with_delay(f"\n{self.name} used {self.moves[index-1]}")
            time.sleep(1)

            print_with_delay(string_1_attack)

            # DETERMINE THE DAMAGE
            pokemon2.bar -= self.attack / 2
            pokemon2.points_of_health = ""
            # add additional bar defense
            for j in range(int(pokemon2.bar + 0.1 * pokemon2.defense)):
                 pokemon2.points_of_health += "="
            time.sleep(1)
            print(f"\n{self.name}\t\tPS\t{self.points_of_health}") 
            print(f"\n{pokemon2.name}\t\tPS\t{pokemon2.points_of_health}") 
            time.sleep(.5)

            # verify damage
            if self.bar <= 0:
                print_with_delay(f"\n...{self.name} is weakened")
                break
            
    def battle(self, pokemon2):
        # Method to simulate the battle between two Pokemon
        # print battle information 
        self.print_Info(pokemon2)
        # consider type information
        string_1_attack, string_2_attack = self.advantage(pokemon2)

        # "Take action!"
        # CONTINUE BATTLE WHILE THE POKEMON HAS HEALTH POINTS
        self.turn(pokemon2, string_1_attack, string_2_attack)

        # Receive a trophy
        money = np.random.choice(5000)
        print_with_delay(f"\nThe opponent receives {money} as a trophy")

if __name__ =='__main__':
    # Main function to run the battle between two Pokemon
    pokemon = pd.read_csv('pokemon game/data/pokemon.csv', index_col="name")
    poke_dex = []

    for i in range(0, 2):
        pokemon_name = input("Pokemon name: ") # Input the name of the Pokemon
        moves_list = eval(pokemon.abilities[pokemon_name]) # Get the moves of the Pokemon
        salvage_Abilitie = moves_list # Save the moves
        salvage_type = pokemon.type1[pokemon_name] # Get the type of the Pokemon
        salvage_SP_attack = pokemon.sp_attack[pokemon_name] # Get the special attack of the Pokemon
        salvage_SP_defense = pokemon.sp_defense[pokemon_name] # Get the special defense of the Pokemon
        salvage = Pokemon(pokemon_name, salvage_type, salvage_Abilitie, {'attack': salvage_SP_attack, 'defense': salvage_SP_defense})
        poke_dex.append(salvage)

    # Start the battle between the two Pokemon
    poke_dex[0].battle(poke_dex[1])
