"""
Implementation of the Wolf, Goat and Cabbage Problem.

Author: Michael Clement
Date: 30 August, 2022
"""

import os

class Game():
    def __init__(self):
        self.playing = True
        self.move_counter = 0
        self.current_shore = "source"
        self.invalid_states = [{"g", "w"}, {"c", "g"}]
        self.shores = {"source": ["w", "g", "c"], "dest"  : []}

    def sail(self, cargo=None):
        if cargo:
            self.shores[self.current_shore].remove(cargo)
            # Toggle the value of "current_shore" between "source" and "dest"
            self.current_shore = "source" if self.current_shore == "dest" else "dest"
            # put the new piece on the destination shore
            self.shores[self.current_shore].append(cargo)
        else:
            self.current_shore = "source" if self.current_shore == "dest" else "dest"

    def check_valid(self):
        for shore in self.shores:
            # Convert the invalid states into sets so we don't have
            # to worry about element order, then check if a shore contains
            # the same elements as an invalid state
            for invalid_state in self.invalid_states:
                if set(self.shores[shore]) == invalid_state and self.current_shore != shore:
                    print(f"\nInvalid state: {self.shores[shore]} on shore {shore}. Game Over.")
                    return False
        return True

    def visualize(self):
        # clear the screen
        os.system('cls||clear')
        print(f"Moves: {self.move_counter}")
        width = 40
        dest_padding   = ((width - (len(self.shores["dest"])*2))//2)
        source_padding = ((width - (len(self.shores["source"])*2))//2)
        water = (("~"*width)+"\n")*3
        d = "."*dest_padding
        s = "."*source_padding
        print("" + d + " ".join(s for s in self.shores["dest"]) + d + ("▣ <- You" if self.current_shore == "dest" else ""))
        print(water[:-1:])
        print(s + " ".join(s for s in self.shores["source"]) + s + ("▣ <- You" if self.current_shore == "source" else ""))

def main():
    game = Game()
    game.visualize()

    while game.playing:
        move = input(
                "\nSelect item to move or press 'Enter' to sail to opposite shore:\n\
                \n\r[W]olf, [G]oat, [C]abbage, or [Q]uit/[R]eset: ").lower()
        if move == "q":
            game.playing = False
        elif move == "r":
            game.__init__()
            game.visualize()
        elif move in game.shores[game.current_shore] or move == "":
            game.sail(move)
            if game.check_valid():
                game.move_counter += 1
                game.visualize()
            else:
                break
            if set(game.shores['dest']) == {"g", "w", "c"}:
                print("\nYou win!")
                break
        else:
            print(f"Invalid input {move}. Try again.")
            continue


if __name__=="__main__":
    main()
