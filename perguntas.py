import pygame

def transforma_em_lista(string):
    # Função que recebe uma string e a transforma em uma lista de listas
    nova_lista = []
    lista = []
    elemento = ""
    chave = False
    for c in string:
        if c == "," and elemento != "":
            lista.append(elemento.strip())
            elemento = ""

        if c == "]":
            lista.append(elemento.strip())
            nova_lista.append(lista)
            lista = []
            elemento = ""
            chave = False

        if chave and c not in ",'[]":
            elemento += c

        if c == "[":
            chave = True

    return nova_lista

    return nova_lista

        


class Pergunta():
    def __init__(self, altA, altB, altC, altD, res, posX, posY):
        self.altA = altA
        self.altB = altB
        self.altC = altC
        self.altD = altD
        self.res = res
        self.posX = posX
        self.posY = posY

    def Escreve_Pergunta(posX, posY, enunciado, res):
        dicio_perguntas = {}
        with open("perguntas.txt", "r", encoding="utf-8") as f:
            linhas = f.readlines()
            for linha in range(len(linhas)):
                if linha % 2 == 0:
                    pergunta = linhas[linha].split(":")
                    dicio_perguntas[pergunta[0]] = pergunta[1]

        for k in dicio_perguntas:
            print("---")
            print(k, transforma_em_lista(dicio_perguntas[k]))

Pergunta.Escreve_Pergunta(1,1,1,1)