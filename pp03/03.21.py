name = 'UEK w Krakowie'
output = ''

for index in range(len(name)):
    if index == 0 or index == len(name):
        output += name[index]
    else:
        #output += " {}".format(name[index])  #  <-- ladnie bez rozbijania na 2 instrukcje
        output += " "
        output += name[index]

print(output)