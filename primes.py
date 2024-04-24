#Реализуйте функцию-генератор primes, которая будет генерировать простые числа в порядке возрастания, начиная с числа 2.
from math import factorial
import itertools
def primes():
    x = 1
    while True:
        x+=1
        if((factorial(x-1)+1)%x==0): # if (p-1)! + 1 divided on p without remainder than p - prime number
            yield x

print(list(itertools.takewhile(lambda x : x <= 31, primes())))

# print (sqrt(9)%1==0)

# print(primes(6))
