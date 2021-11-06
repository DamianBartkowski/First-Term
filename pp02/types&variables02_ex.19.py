

print("podaj bok trójkąta 'a':")
a = int(input())

print("podaj bok trójkąta 'b':")
b = int(input())

print("podaj bok trójkąta 'c':")
c = int(input())

s = (a+b+c) / 2
area = (s*(s-a)*(s-b)*(s-c))**(1/2)
print(area)









