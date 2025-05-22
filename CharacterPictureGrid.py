print("Varun Bellad, 1AY24AI096, Sec-O")
# CharacterPictureGrid.py

grid = [
    ['.', '.', '.', '.', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['.', 'O', 'O', 'O', 'O', 'O'],
    ['O', 'O', 'O', 'O', 'O', '.'],
    ['O', 'O', 'O', 'O', '.', '.'],
    ['.', 'O', 'O', '.', '.', '.'],
    ['.', '.', '.', '.', '.', '.']
]

def print_rotated_grid(g):
    for x in range(len(g[0])):  # columns
        for y in range(len(g)):  # rows
            print(g[y][x], end='')
        print()  # newline after each column

if __name__ == "__main__":
    print_rotated_grid(grid)
