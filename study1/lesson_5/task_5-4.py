dict = {'One': 'один', 'Two': 'два', 'Three': 'три', 'Four': 'четыре'}

with open('text_4.txt') as file, open('text_4-1.txt', 'w') as new_file:
    file_lines=file.readlines()
    for line in file_lines:
        info=line.split()
        ru_num=dict.get(info[0])
        new_file.write(f'{line.replace(info[0], ru_num)}')