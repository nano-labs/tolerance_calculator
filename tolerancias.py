#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import re
from math import sqrt, ceil

mask = u"([0-9]+)([ABCDEFGHJKMNPRSTUVXYZ]+)([0-9]+)([abcdefghjkmnprstuvxyz]+)([0-9]+)"
quit_strings = ["quit", "exit", "sair", "fechar"]

def fD(d):
    d = float(d)
    if d > 0.0 and d <= 1.0:
        m = 0.0
        M = 1.0
    elif d > 1.0 and d <= 3.0:
        m = 1.0
        M = 3.0
    elif d > 3.0 and d <= 6.0:
        m = 3.0
        M = 6.0
    elif d > 6.0 and d <= 10.0:
        m = 6.0
        M = 10.0
    elif d > 10.0 and d <= 14.0:
        m = 10.0
        M = 14.0
    elif d > 14.0 and d <= 18.0:
        m = 14.0
        M = 18.0
    elif d > 18.0 and d <= 24.0:
        m = 18.0
        M = 24.0
    elif d > 24.0 and d <= 30.0:
        m = 24.0
        M = 30.0
    elif d > 30.0 and d <= 40.0:
        m = 30.0
        M = 40.0
    elif d > 40.0 and d <= 50.0:
        m = 40.0
        M = 50.0
    elif d > 50.0 and d <= 65.0:
        m = 50.0
        M = 65.0
    elif d > 65.0 and d <= 80.0:
        m = 65.0
        M = 80.0
    elif d > 80.0 and d <= 100.0:
        m = 80.0
        M = 100.0
    elif d > 100.0 and d <= 120.0:
        m = 100.0
        M = 120.0
    elif d > 120.0 and d <= 140.0:
        m = 120.0
        M = 140.0
    elif d > 140.0 and d <= 160.0:
        m = 140.0
        M = 160.0
    elif d > 160.0 and d <= 180.0:
        m = 160.0
        M = 180.0
    elif d > 180.0 and d <= 200.0:
        m = 180.0
        M = 200.0
    elif d > 200.0 and d <= 225.0:
        m = 200.0
        M = 225.0
    elif d > 225.0 and d <= 250.0:
        m = 225.0
        M = 250.0
    elif d > 250.0 and d <= 280.0:
        m = 250.0
        M = 280.0
    elif d > 280.0 and d <= 315.0:
        m = 280.0
        M = 315.0
    elif d > 315.0 and d <= 355.0:
        m = 315.0
        M = 355.0
    elif d > 355.0 and d <= 400.0:
        m = 355.0
        M = 400.0
    elif d > 400.0 and d <= 450.0:
        m = 400.0
        M = 450.0
    elif d > 450.0 and d <= 500.0:
        m = 450.0
        M = 500.0
    return sqrt(m*M)


def fi(diametro):
    D = float(fD(diametro))
    a = 0.45
    b = 0.001
    return (a*(D**(1.0/3))) + (b*D)

def fIT(diametro, qualidade):
    qualidade = str(qualidade)
    if qualidade == "01":
        return 0.3 + (0.008 * fD(diametro))
    elif qualidade == "0":
        return 0.5 + (0.012 * fD(diametro))
    elif qualidade == "1":
        return 0.8 + (0.020 * fD(diametro))
    elif qualidade == "2":
        q = (fIT(diametro,"5") / fIT(diametro,"1"))**(1.0/4)
        return fIT(diametro, "1") * q
    elif qualidade == "3":
        q = (fIT(diametro,"5") / fIT(diametro,"1"))**(1.0/4)
        return fIT(diametro, "2") * q
    elif qualidade == "4":
        q = (fIT(diametro,"5") / fIT(diametro,"1"))**(1.0/4)
        return fIT(diametro, "3") * q
    elif qualidade == "5":
        return 7.0 * fi(diametro)
    elif qualidade == "6":
        return 10.0 * fi(diametro)
    elif qualidade == "7":
        return 16.0 * fi(diametro)
    elif qualidade == "8":
        return 25.0 * fi(diametro)
    elif qualidade == "9":
        return 40.0 * fi(diametro)
    elif qualidade == "10":
        return 64.0 * fi(diametro)
    elif qualidade == "11":
        return 100.0 * fi(diametro)
    elif qualidade == "12":
        return 160.0 * fi(diametro)
    elif qualidade == "13":
        return 250.0 * fi(diametro)
    elif qualidade == "14":
        return 400.0 * fi(diametro)
    elif qualidade == "15":
        return 640.0 * fi(diametro)
    elif qualidade == "16":
        return 1000.0 * fi(diametro)
    elif qualidade == "17":
        return 1600.0 * fi(diametro)
    elif qualidade == "18":
        return 2500.0 * fi(diametro)



def afastamento(diametro, classe, it):
    if classe == classe.lower():
        furo = False
    else:
        furo = True
    classe = classe.lower()
    if furo:
        if classe == "n" and it >= 9:
            a_s = 0.0
        elif (((classe in ["j", "js", "k", "l", "m", "n"]) and\
                (it in ["01", "0", "1", "2", "3", "4", "5", "6", "7", "8"])) or\
                ((classe in ["p", "r", "s", "t", "u", "v", "x", "y", "z", "za", "zb", "zc"]) and\
                (it in ["01", "0", "1", "2", "3", "4", "5", "6", "7"]))) and (diametro > 3.0):
            # Regra especial
            if it == "0":
                it_menor = "01"
            else:
                it_menor = str(int(it) -1)
            a_s = (afastamento(diametro, classe, it_menor)['ai']) + (fIT(diametro, it) - fIT(diametro, it_menor))
        else:
            #regra geral
            a_s, a_i = afastamento(diametro, classe, it)['as'], afastamento(diametro, classe, it)['ai']
    else: #eh eixo
        if classe == "a":
            if diametro <= 120.0:
                a_s = - (265.0 + 1.3*fD(diametro))
            else:
                a_s = - (3.5*fD(diametro))
        elif classe == "b":
            if diametro <= 160.0:
                a_s = - (140.0 + 0.85*fD(diametro))
            else:
                a_s = - (1.8*fD(diametro))
        elif classe == "c":
            if diametro <= 40.0:
                a_s = - (52.0*(fD(diametro)**0.2))
            else:
                a_s = - (95.0 + 0.8*fD(diametro))
        elif classe == "cd":
            a_s = sqrt(afastamento(diametro, "c", it)['as'] * afastamento(diametro, "d", it)['as'])
        elif classe == "d":
            a_s = -(16.0 * (fD(diametro)**0.44))
        elif classe == "e":
            a_s = -(11.0 * (fD(diametro)**0.41))
        elif classe == "ef":
            a_s = sqrt(afastamento(diametro, "e", it)['as'] * afastamento(diametro, "f", it)['as'])
        elif classe == "f":
            a_s = -(5.5 * (fD(diametro)**0.41))
        elif classe == "g":
            a_s = -(2.5 * (fD(diametro)**0.34))
        elif classe == "h":
            a_s = 0.0
        elif classe == "j":
            # TODO: ENCONTRAR A EQUAÇÃO CORRETA
            pass
        elif classe == "js":
            a_i = - 0.5*fIT(diametro, it)
            a_s = + 0.5*fIT(diametro, it)
        elif classe == "k":
            if (it <= 3) or (it >= 8):
                a_i = 0.0
            else:
                a_i = 0.6 * (fD(diametro)**(1.0/3))
        elif classe == "m":
            a_i = 2.8 * (fD(diametro)**(1.0/3))
        elif classe == "n":
            a_i = 5.0 * (fD(diametro)**0.34)
        elif classe == "p":
            if diametro >= 80.0:
                a_i = 5.6 * (fD(diametro)**0.41)
            else:
                a_i = fIT(diametro, "7") + 2.5
        elif classe == "r":
            a_i = sqrt(afastamento(diametro, "p", it)['ai'] * afastamento(diametro, "s", it)['ai'])
        elif classe == "s":
            if diametro <= 50:
                # TODO: DADO ESTRANHO AQUI: IT7 + (0 a 5)
                a_i = fIT(diametro, "8") + 3
            else:
                a_i = fIT(diametro, "7") + 0.4 * fD(diametro)
        elif classe == "t":
            a_i = fIT(diametro, "7") + 0.63*fD(diametro)
        elif classe == "u":
            a_i = fIT(diametro, "7") + fD(diametro)
        elif classe == "v":
            a_i = fIT(diametro, "7") + 1.25*fD(diametro)
        elif classe == "x":
            a_i = fIT(diametro, "7") + 1.6*fD(diametro)
        elif classe == "y":
            a_i = fIT(diametro, "7") + 2.0*fD(diametro)
        elif classe == "z":
            a_i = fIT(diametro, "7") + 2.5*fD(diametro)
        elif classe == "za":
            a_i = fIT(diametro, "8") + 3.15*fD(diametro)
        elif classe == "zb":
            a_i = fIT(diametro, "9") + 4.0*fD(diametro)
        elif classe == "zc":
            a_i = fIT(diametro, "10") + 5.0*fD(diametro)
        
    if furo:
        a_i = a_s - fIT(diametro, it)
        if classe in ["a", "b", "c", "d", "cd", "e", "f", "ef", "g", "h"]:
            a_i = a_s - fIT(diametro, it)
        else:
            a_s = fIT(diametro, it) - a_i
        return {"As": arredondamento(-a_i, classe), "Ai": arredondamento(-a_s, classe)}
    else: # eh eixo
        if classe in ["a", "b", "c", "d", "cd", "e", "f", "ef", "g", "h"]:
            a_i = a_s - fIT(diametro, it)
        else:
            a_s = fIT(diametro, it) - a_i
        return {"as": arredondamento(a_s, classe), "ai": arredondamento(a_i, classe)}

def arredondamento(a, classe):
    negative = False
    if a < 0:
        negative = True
        a = -a
    if classe in ["a", "b", "c", "cd", "d", "e", "ef", "f", "g"]:
        if a <= 45:
            a = ceil(a)
        elif a > 45 and a <= 60:
            a = int(a/2)*2
        elif a > 60 and a <= 200:
            a = int(a/5)*5
        elif a > 200 and a <= 560:
            a = int(a/10)*10
        elif a > 560 and a <= 1000:
            a = int(a/20)*20
        elif a > 1000 and a <= 2000:
            a = int(a/50)*50
    else:
        if a <= 100:
            a = ceil(a)
        elif a > 100 and a <= 300:
            a = int(a/2)*2
        elif a > 300 and a <= 600:
            a = int(a/5)*5
        elif a > 600 and a <= 800:
            a = int(a/10)*10
        elif a > 800 and a <= 1000:
            a = int(a/20)*20
        elif a > 1000 and a <= 2000:
            a = int(a/50)*50
        elif a > 2000:
            a = int(a/100)*100
    if negative:
        return -a
    else:
        return a

def calculator(encaixe):
    """"Calcula os valores de afastamentos com base na norma ABNT NBR 6158."""
    match = re.match(mask, encaixe)
    if not match:
        raise Exception("Valor invalido.")
    tol_corrigida = match.group(0)
    diametro = match.group(1)
    diametro = float(diametro)
    classe_furo = match.group(2)
    it_furo = match.group(3)
    classe_eixo = match.group(4)
    it_eixo = match.group(5)
    i = fi(diametro)
    afastamentos_furo = afastamento(diametro, classe_furo, it_furo)
    afastamentos_eixo = afastamento(diametro, classe_eixo, it_eixo)
    A_s = ceil(afastamentos_furo['As'])
    A_i = ceil(afastamentos_furo['Ai'])
    a_s = ceil(afastamentos_eixo['as'])
    a_i = ceil(afastamentos_eixo['ai'])
    return {"diameter": diametro,
            "hub": {"fit": "%s%s" % (classe_furo, it_furo),
                    "upper": A_s,
                    "lower": A_i,
                    "mid": ceil((A_s + A_i)/2.0)},
            "shaft": {"fit": "%s%s" % (classe_eixo, it_eixo),
                      "upper": a_s,
                      "lower": a_i,
                      "mid": ceil((a_s + a_i)/2.0)},
            "clearance": {"max": A_s - a_i,
                          "min": A_i - a_s,
                          "mid": ceil(((A_s - a_i) + (A_i - a_s))/2.0)}}



if __name__ == "__main__":
    print "Digite a tolerância:"
    while 1:
        tolerancia = raw_input()
        if tolerancia in quit_strings:
            break
        match = re.match(mask,tolerancia)
        if match:
            tol_corrigida = match.group(0)
            diametro = match.group(1)
            classe_furo = match.group(2)
            it_furo = match.group(3)
            classe_eixo = match.group(4)
            it_eixo = match.group(5)
            i = fi(diametro)
            afastamentos_furo = afastamento(diametro, classe_furo, it_furo)
            afastamentos_eixo = afastamento(diametro, classe_eixo, it_eixo)
            A_s = ceil(afastamentos_furo['As'])
            A_i = ceil(afastamentos_furo['Ai'])
            a_s = ceil(afastamentos_eixo['as'])
            a_i = ceil(afastamentos_eixo['ai'])
            print "Conjunto ø%s" % (tol_corrigida)
            print "FURO %s%s:\tAs: %dµm \tAi: %dµm \tMédia: %dµm" % (classe_furo, it_furo, A_s, A_i, ceil((A_s + A_i)/2.0))
            print "EIXO %s%s:\tas: %dµm \tai: %dµm \tMédia: %dµm" % (classe_eixo, it_eixo, a_s, a_i, ceil((a_s + a_i)/2.0))
            print "Folga máxima: %dµm\tFolga mínima: %dµm\tFolga média: %dµm" % ((A_s - a_i), (A_i - a_s), ceil(((A_s - a_i) + (A_i - a_s))/2.0))
            print ""
        else:
            print "Tolerância não identificada. Tente novamente."