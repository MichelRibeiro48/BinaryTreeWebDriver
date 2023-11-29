import functools

def compararListas(numeros, numeros2, operacao): 
  lista = numeros.split('(')
  lista = [s.strip(')') for s in lista]
  lista.pop(0)
  lista2 = numeros2.split(',')
  lista2 = [s.strip(' ') for s in numeros2]
  if (operacao == '1'):
    if functools.reduce(lambda x, y : x and y, map(lambda p, q: p == q,lista2,lista), True):
      print ("Passou")
    else:
      print ("Não Passou")
  if (operacao == '2'):
    meio = int(len(lista) / 2)
    raiz = lista[0]
    lista.pop(0)
    novalista = lista[0:meio] + [raiz] + lista[meio:]
    print(novalista)


compararListas('(28(9(8))(42(79)))', '28, 9, 8, 42, 79', '2')
# print(' '.join(map(str, lista)))