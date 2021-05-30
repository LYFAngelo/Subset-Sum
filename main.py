import itertools
import random
from time import time

def bruteforce(x_list, target):
    possiblities = []
    for x in powerset(x_list):
        possiblities.append((x, sum(x)))

    x_list, actual_value = closest(possiblities, target)

    return (actual_value, x_list)


def powerset(iterable):
    s = list(iterable)
    return itertools.chain.from_iterable(itertools.combinations(s, r) for r in range(len(s) + 1))


def closest(possiblities, target):
    return min((abs(target - total), (o_list, total))
               for o_list, total in possiblities)[1]

        
def main():
    x_list = []
    for i in range(0,5):                        
        num = random.randint(0,100)               
        x_list.append(num) 
    target = random.randint(0,100) 

    time0 = time()
    bf = bruteforce(x_list, target)
    time1 = time()

    print(x_list)
    print(target)
    print('Brute force:', bf, time1 - time0)

if __name__ == '__main__':
    main()
