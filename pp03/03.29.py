n = 1
suma= 0
quantity = 0
while n != 0:
    n = int(input())
    suma += n
    quantity += 1


mean = suma/quantity
print("Quantity:",quantity)
print("sum:",suma)
print("mean:",mean)