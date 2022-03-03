with open('text2.txt', 'r') as file:
    content = file.readlines()
    print(f'Количество строк в файле - {len(content)}')

for i in range(len(content)):
    print(f'кoличество символов {i + 1} - ой строки {len(content[i])}')
my_file = open('text2.txt', 'r')
content = my_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
