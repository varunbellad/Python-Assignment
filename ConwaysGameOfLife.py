print("Varun Bellad, 1AY24AI096, Sec-O")
# ConwaysGameOfLife.py

import random
import time
import copy
import os

WIDTH = 40
HEIGHT = 20

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def create_grid():
    return [[random.choice([' ', '#']) for _ in range(WIDTH)] for _ in range(HEIGHT)]

def print_grid(grid):
    for row in grid:
        print(''.join(row))

def get_neighbor_count(grid, x, y):
    count = 0
    for dy in (-1, 0, 1):
        for dx in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            nx, ny = (x + dx), (y + dy)
            if 0 <= nx < WIDTH and 0 <= ny < HEIGHT:
                if grid[ny][nx] == '#':
                    count += 1
    return count

def update_grid(grid):
    new_grid = copy.deepcopy(grid)
    for y in range(HEIGHT):
        for x in range(WIDTH):
            neighbors = get_neighbor_count(grid, x, y)
            if grid[y][
