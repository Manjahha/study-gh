from itertools import count, cycle

start = int(input('Start number: '))
stop = start * 2 + 5

for i in count(start):
    if i < stop:
        print(i)
    else:
        break
del i

my_list = [i for i in range(stop)]
count = 0
for b in cycle(my_list):
    if count < stop + 10:
        print(b)
        count += 1
    else:
        break
