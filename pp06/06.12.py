lista = [15, 8, 31, 47, 2, 19]
lenght = len(lista)
reverse_list = []
while lenght > 0:
    reverse_list.append(lista[lenght-1])
    lenght = lenght -1
print(reverse_list)
