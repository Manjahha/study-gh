with open('text3.txt') as file:
    lines=file.readlines()

dict={}
sal=0
for line in lines:
    dict_str=line.split()
    dict.update({dict_str[0]: int(dict_str[1])})
    sal+=float({dict_str[1]})
average=sal/ len(dict)
print(f'average salary ={average}')

