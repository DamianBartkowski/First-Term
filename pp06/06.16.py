def star(n):
    for i in array:
        if 10 <= i <= 99:
            print(f'{i}: {symbol * i}')
        else:
            print(f'{i}:  {symbol * i}')
symbol = '*'
array = [12, 6, 4, 9, 3]

print(star(array))