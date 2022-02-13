import os
import random


def generate_map(name, width, height):
    line = ''
    ans = []
    for i in range(height):
        for j in range(width):
            if random.choice([0, 1]) == 0:
                line += '.'
            else:
                line += '#'
        ans.append(line)
        line = ''
    with open(os.path.join('maps', name), 'w') as map_file:
        for i in range(len(ans) - 1):
            map_file.write(ans[i] + '\n')
        map_file.write(ans[-1])


generate_map('random_map.txt', 20, 18)
