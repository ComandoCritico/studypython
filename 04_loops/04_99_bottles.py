for i in range(100, 0, -1):
    print(f'{i} bottles of beer on the wall')
    print(f'{i} bottles of beer')
    print('Take one down, pass it around')
    if i == 1:
        print('No more bottles of beer on the wall!')
        break