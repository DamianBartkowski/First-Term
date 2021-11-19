def count_e_letter():
    text = 'You never get a second chance to make a first impression'
    len(text)
    amount = 0
    for index in range(len(text)):
        if (text[index] == "e"):
            amount +=1
    print(amount)
count_e_letter()
