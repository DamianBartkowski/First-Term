print("podaj swoją wagę w kg:")
weight = float(input())
print("podaj swój wzrost w cm:")
height = float(input())
BMI = weight/(height/100)**2
print("Twoje BMI wynosi:", BMI)
