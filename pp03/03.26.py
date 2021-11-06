PIN = "0412"
attempts = 0
for i in range(3):
    attempts += 1
    pin = str(input("Enter PIN:"))
    if pin == PIN:
        print("Correct PIN!")
        break
    elif pin != PIN:
        print("Incorrect PIN")
if attempts == 3:
        print("Sorry, your payment card has been blocked.")

