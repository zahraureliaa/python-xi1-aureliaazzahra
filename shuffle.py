import itertools, random

deck = list(itertools.product(range(1,14),['kriting','wajik','sekop']))

random.shuffle(deck)
print('Kamu mendapat: ')
for i in range(5):
    print(deck[i][0], ' dari', deck[i][1])