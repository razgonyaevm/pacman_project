import os
import random


def generate_map(name, width, height, coin=100000):
    """Функция для генерирования карт уровней. name - название файля для сохранения,
    файл автоматически сохраняется в апку maps;
    width - длина каждой строчки
    height - количество строк в файле (не 0)
    coin - необязательный параметр, нужен для упрощения уровня (ограничивает количество блоков в каждой строке)
    При этом нижние, верхние и боковые линии должны быть свободны от блоков"""

    line = ''
    correct = 0
    ans = ['.' * width]
    for i in range(height - 2):
        line += '.'
        for j in range(width - 2):
            if correct < coin:
                if random.choice([0, 1, 2, 3, 4, 5]) == 0:
                    line += '#'
                    correct += 1
                else:
                    line += '.'

            else:
                line += '.'
        line += '.'
        ans.append(line)
        line = ''
        correct = 0
    ans.append('.' * width)
    with open(f'maps/{name}', 'w') as map_file:
        for i in range(len(ans) - 1):
            map_file.write(ans[i] + '\n')
        map_file.write(ans[-1])


if __name__ == '__main__':
    generate_map('new_map.txt', 20, 18, 5)
