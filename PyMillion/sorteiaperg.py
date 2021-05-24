from random import randint, sample

def sorteiaPergunta(list):

    n = randint(0, len(list)-1)

    a,b,c,d = sample(range(1,5),4)
    
    perg = list[n][0][0]
    res = list[n][0][1]
    a = list[n][a]
    b = list[n][b]
    c = list[n][c]
    d = list[n][d]
    list.pop(n)
    lista = list
    return perg, res, a, b, c, d, lista