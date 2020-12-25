#! python3

import string
import random

# initialization of variables
width, height = 20, 20
grid = [['_' for j in range(width)] for i in range(height)]
words = ['HELLO', 'THERE', 'FRIEND']

# functions
def print_grid(grid):
    print('\n'.join(map(lambda row: ' '.join(row), grid)))

def construct_word(word, grid):

    is_placed = False
    max_x_pos, max_y_pos, selected_x_pos, selected_y_pos = 0, 0, 0, 0
    
    while is_placed == False: 
        orientations = [[1, 0], [0, 1], [1, 1]]
        selected_orientation = random.choice(orientations)

        max_x_pos = len(grid) if selected_orientation[0] == 0 else len(grid)-len(word)
        max_y_pos = len(grid[0]) if selected_orientation[1] == 0 else len(grid[0])-len(word)

        selected_x_pos = random.randrange(0, max_x_pos)
        selected_y_pos = random.randrange(0, max_y_pos)

        for i in range(0, len(word)):
            pos_to_place = grid[selected_y_pos + (selected_orientation[1] * i)][selected_x_pos + (selected_orientation[0] * i)]
            if pos_to_place == '_' or pos_to_place == word[i]:
                is_placed = True
                continue
            else:
                is_placed = False
                break

    if is_placed == True:
        for i in range(0, len(word)):
            grid[selected_y_pos + (selected_orientation[1] * i)][selected_x_pos + (selected_orientation[0] * i)] = word[i]

def construct_words(words, grid):
    for i in range(0, len(words)):
        construct_word(words[i], grid)

# main
construct_words(words, grid)
print_grid(grid)


