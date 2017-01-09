import os


def sis(dato):
    paso = os.popen(dato)
    dato2 = paso.readlines()
    return dato2


def sisnom(dato1):
    paso1 = os.popen(dato1)
    dato5 = paso1.readlines()
    pc = dato5[0].split(" ")[-1].split("\n")[0]
    return pc


def sred(dato2, x):
    red = dato2(9).split(" : ")[-1].split("\n")[0]
    infW = x + " name= " + red + " key=clear "
    w = os.popen(infW)
    r = w.readlines()
    return r

nom = "hostname"
com = "netsh wlan show profile"

dw = sis(com)
nom_pc = sisnom(nom)

num = len(dw) - 10
i = 1

nom_fich = nom_pc + ".txt"
fichero = open(nom_fich, "w")

while i <= num:
    com = "netsh wlan show profile"
    df = dw.pop(9).split(" : ")[-1].split("\n")[0]
    red = com + " name= " + df + " key=clear "
    w = os.popen(red)
    r = w.readlines()
    try:
        nomUsu = r[10].split(" : ")[-1].split("\n")[0]
        passUsu = r[32].split(" : ")[-1].split("\n")[0]
        passUs = r[30].split(" : ")[-1].split("\n")[0]
        infWf = "User: " + nomUsu
        infWf1 = " Pass: " + passUsu + " " + passUs
        esPa = "\n"
        es = infWf + " " + infWf1 + esPa
        fichero.writelines(es)
    except:
         print i
    print es
    i = i + 1
fichero.close()


