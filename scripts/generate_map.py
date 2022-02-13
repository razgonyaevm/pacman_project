import os
import random


def generate_map(name, width, height, coin=100000):
    """Функция для генерирования карт уровней. name - название файля для сохранения,
    файл автоматически сохраняется в апку maps;
    width - длина каждой строчки
    height - количество строк в файле (не 0)
    coin - необязательный параметр, нужен для упрощения уровня (ограничивает количество блоков в каждой строке)"""

    line = ''
    correct = 0
    ans = []
    for i in range(height):
        for j in range(width):
            if correct < coin:
                if random.choice([0, 1]) == 0:
                    line += '.'
                else:
                    line += '#'
                    correct += 1
            else:
                line += '.'
        ans.append(line)
        line = ''
        correct = 0
    with open(os.path.join('maps', name), 'w') as map_file:
        for i in range(len(ans) - 1):
            map_file.write(ans[i] + '\n')
        map_file.write(ans[-1])


generate_map('random_map.txt', 20, 18)