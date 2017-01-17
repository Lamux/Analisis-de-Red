import os


def __init__ (self):
    print "inicio"

def sis():
    com = "netsh wlan show profile"
    paso = os.popen(com)
    dato2 = paso.readlines()
    return dato2


def sisnom():
    nom = "hostname"
    paso1 = os.popen(nom)
    dato5 = paso1.readlines()
    pc = dato5[0].split(" ")[-1].split("\n")[0]
    return pc


def sred(dato2):
    com = "netsh wlan show profile"
    infW = com + " name= " + '"' + dato2 + '"' + " key=clear "
    w = os.popen(infW)
    r = w.readlines()
    return r

dw = sis()
nom_pc = sisnom()

num = len(dw) - 10
i = 1

nom_fich = nom_pc + ".txt"
fichero = open(nom_fich, "w")

while i <= num:
    df = dw.pop(9).split(" : ")[-1].split("\n")[0]
    r = sred(df)
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
    print df
    i = i + 1
fichero.close()


