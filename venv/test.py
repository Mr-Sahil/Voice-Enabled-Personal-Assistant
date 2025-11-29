with open("D:\\myData\\myEmail\\email.txt") as f1:
        Econtents = f1.readlines()
with open("D:\\myData\\myEmail\\pass.txt") as f2:
        Pcontents = f2.readlines()
print(Econtents[0], Pcontents)
f1.close()
f2.close()
