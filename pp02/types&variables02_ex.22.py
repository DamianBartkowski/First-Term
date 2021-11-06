import random

roll = random.randint(1, 6)

print("podaj liczbe od 1 do 6:")
guess = int(input())
while guess != roll:
    print("Źle! Spróbój jeszcze raz!")
    guess = int(input())
if guess == roll:
    print("Dobrze!")






