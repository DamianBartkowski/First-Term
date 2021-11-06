dog_years = int(input("Enter the dog's age in human years: "))
in_human_years = 0
for i in range(dog_years):
    if i < 2:
        in_human_years += 10.5
    else:
        in_human_years += 4




print(in_human_years)


