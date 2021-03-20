#Turma C
#O Felipe e a Isabela são da turma C e o David é da turma H
#Equipe Euler
#David Fanchic Chatelard - 180052411
#Felipe Daia Leão Santos - 180041681
#Isabela Salgado Oliveira - 180018981


import matplotlib.pyplot as plt
import numpy as np
import csv
from matplotlib.backends.backend_pdf import PdfPages

facul = open("faculdades.csv","r",encoding = "ISO-8859-1", newline = '')
reader = csv.reader(facul,delimiter = ";")
next(reader, None)
dic = {}
dic2 = {}
dic3 = {}

for coluna in reader:
    if coluna[5] == '1':
        if coluna[6] in dic:
            dic[coluna[6]] += 1
        else:
            dic[coluna[6]] = 1
        if coluna[17] == '1':
            if coluna[6] in dic2:
                dic2[coluna[6]] += 1
            else:
                dic2[coluna[6]] = 1
        if coluna[17] == '2':
            if coluna[6] in dic3:
                dic3[coluna[6]] += 1
            else:
                dic3[coluna[6]] = 1
    elif coluna[5] == '2':
        if coluna[6] in dic:
            dic[coluna[6]] += 1
        else:
            dic[coluna[6]] = 1
        if coluna[17] == '1':
            if coluna[6] in dic2:
                dic2[coluna[6]] += 1
            else:
                dic2[coluna[6]] = 1
        if coluna[17] == '2':
            if coluna[6] in dic3:
                dic3[coluna[6]] += 1
            else:
                dic3[coluna[6]] = 1
    elif coluna[5] == '3':
        if coluna[6] in dic:
            dic[coluna[6]] += 1
        else:
            dic[coluna[6]] = 1
        if coluna[17] == '1':
            if coluna[6] in dic2:
                dic2[coluna[6]] += 1
            else:
                dic2[coluna[6]] = 1
        if coluna[17] == '2':
            if coluna[6] in dic3:
                dic3[coluna[6]] += 1
            else:
                dic3[coluna[6]] = 1
    elif coluna[5] == '4':
        if coluna[6] in dic:
            dic[coluna[6]] += 1
        else:
            dic[coluna[6]] = 1
        if coluna[17] == '1':
            if coluna[6] in dic2:
                dic2[coluna[6]] += 1
            else:
                dic2[coluna[6]] = 1
        if coluna[17] == '2':
            if coluna[6] in dic3:
                dic3[coluna[6]] += 1
            else:
                dic3[coluna[6]] = 1
    elif coluna[5] == '5':
        if coluna[6] in dic:
            dic[coluna[6]] += 1
        else:
            dic[coluna[6]] = 1
        if coluna[17] == '1':
            if coluna[6] in dic2:
                dic2[coluna[6]] += 1
            else:
                dic2[coluna[6]] = 1
        if coluna[17] == '2':
            if coluna[6] in dic3:
                dic3[coluna[6]] += 1
            else:
                dic3[coluna[6]] = 1



regioes = dic.keys()
y_pos = np.arange(len(regioes))
num_facul = dic.values()
fig = plt.figure()
graf = fig.add_subplot(111)
rects = graf.bar(y_pos, num_facul, align="center", alpha=0.5, color='blue')
graf.set_xticks(y_pos)
graf.set_xticklabels(list(dic.keys()))
graf.set_ylabel("Número de faculdades")
graf.set_xlabel("Regiões")
graf.set_title("Número de faculdades por região")
plt.grid(True)

regioes2 = dic2.keys()
y2_pos = np.arange(len(regioes2))
num2_facul = dic2.values()
fig2 = plt.figure()
graf2 = fig2.add_subplot(111)
rects2 = graf2.bar(y2_pos, num2_facul, align="center", alpha=0.5, color='green')
graf2.set_xticks(y2_pos)
graf2.set_xticklabels(list(dic2.keys()))
graf2.set_ylabel("Número de faculdades Públicas")
graf2.set_xlabel("Regiões")
graf2.set_title("Número de faculdades Públicas por região")
plt.grid(True)

regioes3 = dic3.keys()
y3_pos = np.arange(len(regioes3))
num3_facul = dic3.values()
fig3 = plt.figure()
graf3 = fig3.add_subplot(111)
rects3 = graf3.bar(y3_pos, num3_facul, align="center", alpha=0.5, color='red')
graf3.set_xticks(y3_pos)
graf3.set_xticklabels(list(dic3.keys()))
graf3.set_ylabel("Número de faculdades Privadas")
graf3.set_xlabel("Regiões")
graf3.set_title("Número de faculdades Privadas por região")
plt.grid(True)

with PdfPages('Ttrabalho8_turma_C_equipe_Euler.pdf') as pdf:
    lastPage = plt.figure(figsize=(11.69,8.27))
    lastPage.clf()
    ttx = ('Turma C')
    ttx2 = ('O Felipe e a Isabela são da turma C e o David é da turma H')
    ttx1 = ('Equipe Euler')
    ttx3 = ('David Fanchic Chatelard - 180052411')
    ttx4 = ('Felipe Daia Leão Santos - 180041681')
    ttx5 = ('Isabela Salgado Oliveira - 180018981')
    lastPage.text(0.5,0.8,ttx, transform=lastPage.transFigure, size=24, ha="center")
    lastPage.text(0.5,0.7,ttx2, transform=lastPage.transFigure, size=24, ha="center")
    lastPage.text(0.5,0.6,ttx1, transform=lastPage.transFigure, size=24, ha="center")
    lastPage.text(0.5,0.5,ttx3, transform=lastPage.transFigure, size=24, ha="center")
    lastPage.text(0.5,0.4,ttx4, transform=lastPage.transFigure, size=24, ha="center")
    lastPage.text(0.5,0.3,ttx5, transform=lastPage.transFigure, size=24, ha="center")
    firstPage = plt.figure(figsize=(11.69,8.27))
    firstPage.clf()
    txt = ("A partir dos dados apresentados, percebe-se que o Sudeste")
    txt1 =("tem o maior índice de faculdades do Brasil, apesar")
    txt2=("de ser a segunda menor região é a que possui maior")
    txt3=("concentração populacional e uma das mais desenvolvida do país,")
    txt4=("tal índice elevado também tem relação com a industrialização")
    txt5=("e economia do Brasil, que por sua vez é uma das mais")
    txt6 = ('importantes para o desenvolvimento do mesmo. ')
           
    firstPage.text(0.5,0.8,txt, transform=firstPage.transFigure, size=24, ha="center")
    firstPage.text(0.5,0.7,txt1, transform=firstPage.transFigure, size=24, ha="center")
    firstPage.text(0.5,0.6,txt2, transform=firstPage.transFigure, size=24, ha="center")
    firstPage.text(0.5,0.5,txt3, transform=firstPage.transFigure, size=24, ha="center")
    firstPage.text(0.5,0.4,txt4, transform=firstPage.transFigure, size=24, ha="center")
    firstPage.text(0.5,0.3,txt5, transform=firstPage.transFigure, size=24, ha="center")
    firstPage.text(0.5,0.2,txt6, transform=firstPage.transFigure, size=24, ha="center")
    pdf.savefig(lastPage)
    pdf.savefig(fig)
    pdf.savefig(fig2)
    pdf.savefig(fig3)
    pdf.savefig(firstPage)
