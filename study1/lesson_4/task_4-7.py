def gen_factorial(number):
    count = 1
    for i in range(1,number+1):
        count*=i
        yield count
n=12
for ind, el in enumerate(gen_factorial(n)):
    print(el)
