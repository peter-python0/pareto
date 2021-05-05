import random
import sys

dict = {
    'peter': 1000,
    'lucinda': 1000,
    'mike': 1000,
    }

counter = 0

while dict['peter'] != 5000 and dict['lucinda'] != 5000 and dict['mike'] != 5000:
    key1 = random.choice(list(dict))
    key2 = random.choice(list(dict))

    while dict[key1] <= 0:
        key1 = random.choice(list(dict))

    while dict[key2] <= 0:
        key2 = random.choice(list(dict))

    quot = dict[key1]/dict[key2]

    lst = ['heads', 'heads', 'heads', 'heads', 'heads', 'tails']
    lst1 = ['heads', 'heads', 'heads', 'tails']
    lst2 = ['heads', 'tails']
    lst3 = ['heads', 'tails', 'tails', 'tails']
    lst4 = ['heads', 'tails', 'tails', 'tails', 'tails', 'tails']

    if quot < 0.3:
        b = lst
        if counter % 10 == 0:
            dict[key1] += 50
            dict[key2] -= 50
    elif quot >= 0.3 and quot < 0.7:
        b = lst1
        if counter % 10 == 0:
            dict[key1] += 50
            dict[key2] -= 50
    elif quot >= 0.7 and quot < 1.43:
        b = lst2
    elif quot >= 1.43 and quot < 3.33:
        b = lst3
        if counter % 10 == 0:
            dict[key2] += 50
            dict[key1] -= 50
    else:
        b = lst4
        if counter % 10 == 0:
            dict[key2] += 50
            dict[key1] -= 50

    a = random.choice(b)

    if a == 'heads':
        dict[key2] += 10
        dict[key1] -= 10
    else:
        dict[key1] += 10
        dict[key2] -= 10

    print(dict)


    for i in dict:
        if dict[i] == 3000:
            sys.exit()

    if key1 == key2:
        counter = counter
    else:
        counter += 1
    print(counter)
