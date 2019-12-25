import random
import itertools

def randoms(min, max, any_bonus):
    while True:
        yield random.randint(min + any_bonus, max + any_bonus)

rand_atacks = randoms(1, 20, 2)
need_ataks = list(itertools.islice(rand_atacks, 5))
print(need_ataks)