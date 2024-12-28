import copy


testing = False
sample = 2

if testing:
    file_name = 'day_15_sample_big.dat' if sample == 2 else 'day_15_sample_small.dat'
else:
    file_name = 'day_15.dat'

with open(file_name) as f:
    raw = f.read().strip().split('\n\n')
    raw[0] = [list(x) for x in raw[0].splitlines()]
    grid = copy.deepcopy(raw[0])
    movements = raw[1].replace("\n", "")
    for idx, r in enumerate(raw[0]):
        if '@' in r:
            robot = [idx, r.index('@')]
            

"""
########
#..O.O.#
##@.O..#
#...O..#
#.#.O..#
#...O..#
#......#
########

<^^>>>vv<v>>v<<
"""

for g in grid:
    print(g)

print("movements", movements)
print(f"{robot = }")

def move_robot(move):
    cardinals = {"^" : (-1, 0), "v" : (1, 0), "<" : (0, -1), ">" : (0, 1)}
    
    dr, dc = cardinals[move]

    possible_moves = []
    current_r, current_c = robot

    while grid[current_r][current_c] not in "#.":
        print("I append:", current_r, current_c)
        possible_moves.append((current_r, current_c))
        current_r += dr
        current_c += dc
        print("Next check:", current_r, current_c)

    while possible_moves:
        cand_r, cand_c = possible_moves.pop()
        next_r = cand_r + dr
        next_c = cand_c + dc

        if grid[next_r][next_c] == '.':
            grid[next_r][next_c] = grid[cand_r][cand_c]
            grid[cand_r][cand_c] = '.'
            if grid[next_r][next_c] == '@':
                robot[0] = next_r
                robot[1] = next_c
        else:
            print("WARNING")
            break

for move in movements:
    move_robot(move)


final = [list(x) for x in """########
#....OO#
##.....#
#.....O#
#.#O@..#
#...O..#
#...O..#
########""".splitlines()]

print("Success? ", final == grid)

if not final == grid:
    print("Error?")
    for g in grid:
        print(g)
    
def compute_GPS_coord(grid):
    gps = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 'O':
                gps += r * 100 + c
    return gps

print(f"GPS = {compute_GPS_coord(grid)}")
