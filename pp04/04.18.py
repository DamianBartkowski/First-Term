def sum_of_digits(n):
    x = str(n)
    len(x)
    suma = 0
    for index in range(len(x)):
        suma += int(x[index-1])
    print(suma)


sum_of_digits(125)
