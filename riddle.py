import string


rid = open("FirstRiddleOK.txt", "r")
rig = rid.read()
alpha_list = str(string.ascii_lowercase)


fin_list = []

for i in (rig):
    if i == " " or i == "\n":
        fin_list.append(i)
    elif i.isupper():
        i = i.lower()
        i = alpha_list[-alpha_list.index(i) - 1]
        i = i.upper()
        fin_list.append(i)
    else:
        i = alpha_list[-alpha_list.index(i) - 1]
        fin_list.append(i)
        
rij = ("".join(fin_list))

print(rij)













#def decypher(x):
