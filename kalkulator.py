import re

regnestykke = "10/5*2+5-3"

operators = "[+-/*]"

splited = re.split(operators, regnestykke)

for i, ele in enumerate(splited):
    splited[i] = float(ele)
print(splited)
operatorlist = re.findall(operators, regnestykke)
print(operatorlist)

charrekk = ["*", "/", "+", "-"]

gangeind = ""
deleind = ""

while (charrekk[0] in operatorlist) or (charrekk[1] in operatorlist):


    if (charrekk[0] in operatorlist):
        gangeind = operatorlist.index("*")

    else:
        gangeind = ""
    if (charrekk[1] in operatorlist):
        deleind = operatorlist.index("/")

    else:
        deleind=""



    if (gangeind != "") and (deleind != ""):

        if gangeind > deleind:
            splited[deleind] = splited[deleind] / splited[deleind + 1]
            splited.pop(deleind + 1)
            operatorlist.remove("/")
        else:
            splited[gangeind] = splited[gangeind] * splited[gangeind + 1]
            splited.pop(gangeind + 1)
            operatorlist.remove("*")
    elif gangeind != "":

        splited[gangeind] = splited[gangeind] * splited[gangeind + 1]
        splited.pop(gangeind + 1)
        operatorlist.remove("*")
    else:

        splited[deleind] = splited[deleind] / splited[deleind + 1]
        splited.pop(deleind + 1)
        operatorlist.remove("/")

plussind = ""
deleind = ""

while (charrekk[2] in operatorlist) or (charrekk[3] in operatorlist):


    if (charrekk[2] in operatorlist):
        plussind = operatorlist.index("+")

    else:
        plussind = ""
    if (charrekk[3] in operatorlist):
        minusind = operatorlist.index("-")

    else:
        minusind = ""



    if (plussind != "") and (minusind != ""):

        if plussind > minusind:
            splited[minusind] = splited[minusind] - splited[minusind + 1]
            splited.pop(minusind + 1)
            operatorlist.remove("-")
        else:
            splited[plussind] = splited[plussind] + splited[plussind + 1]
            splited.pop(plussind + 1)
            operatorlist.remove("+")
    elif plussind != "":

        splited[plussind] = splited[plussind] + splited[plussind + 1]
        splited.pop(plussind + 1)
        operatorlist.remove("+")
    else:

        splited[minusind] = splited[minusind] - splited[minusind + 1]
        splited.pop(minusind + 1)
        operatorlist.remove("-")




print(operatorlist,splited)
print(f' Tallet er {splited[0]}')
"""
for char of charrekk
while charrekk[0] in operatorlist:
    ind = operatorlist.index("*")
    i

"""

"""
character = ["+", "-", "*", "/"]
foundChar = []
for cha in character:

    try:
        regnestykke.index(cha)

    except ValueError:
        continue
    else:
        foundChar.append(cha)

splregn = ""
if * in
"""
