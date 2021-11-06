



for num in range(30):

    num+=1
    if num%3==0 and num%5==0:
        print("BINGO")
    elif num%3==0:
        print("three")
    elif num%5==0:
        print("Five")
    else:
        print(num)


