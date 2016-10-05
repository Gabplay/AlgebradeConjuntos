#coding: UTF-8
#Functions called in gui_conjuntos.py
import sys

def ordenaVetor(vetor):
	#Ordena em ordem crescente
	for i in range(len(vetor) - 1):
		for j in range(len(vetor) - 1):
			if vetor[j] > vetor[j + 1]:
				aux = vetor[j]
				vetor[j] = vetor[j + 1]
				vetor[j + 1] = aux
	vetor = list(set(vetor)) #Remove itens duplicados
	return vetor

def uniao(a, b):
	#Elementos de A e elementos de B
    uniao = []
    for i in range(0, len(a)):
        uniao.append(a[i])
    for j in range(0, len(b)):
        uniao.append(b[j])
    uniao = ordenaVetor(uniao)
    return uniao
 
def intersecao(a, b):
	#Elementos comuns ao conjunto A e ao conjunto B
    inter = []
    for j in range(0, len(b)):
        for i in range(0, len(a)):
            if (a[i] == b[j]):
                inter.append(a[i])
    inter = ordenaVetor(inter)
    return inter
 
def diferenca(a, b):
	#Elementos exclusivos de A
    for j in range(0, len(b)):
        for i in range(0, len(a)):
            if (a[i] == b[j]):
                a[i] = 'null'
    #Substitui interseções por 0 e as remove
    while a.count('null') > 0:
        a.remove('null')
    a = ordenaVetor(a)
    return a

def difSimetrica(a, b):
	#Elementos de A ou elementos de B mas não de ambos
	difS = uniao(a, b)
	inter = intersecao(a, b)

	for i in range(0, len(difS)):
		for j in range(0, len(inter)):
			if(difS[i] == inter[j]):
				difS[i] = 'null'
	#União - Interseção
	while difS.count('null') > 0:
		difS.remove('null')
	return difS
