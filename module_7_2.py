from idlelib.iomenu import encoding
from pprint import pprint

def custom_write(file_name, strings):
    strings_positions = {}
    file = open(file_name, 'w', encoding='utf-8')
    num_lane = 1

    for n in strings:
        position = file.tell()
        file.write(f'{n}\n')
        strings_positions[(num_lane, position)] = n
        num_lane += 1

    file.close()
    return strings_positions
info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)






