def velocidademedia(velocidade, distancia):
    vm = distancia/velocidade
    return vm
def lernome():
    nome = input('Digite o seu nome: ')
    return nome
def tamanhonome(nome):
    nome2 = nome.strip()
    nome2 = nome.split()
    nome = ''.join(nome2)
    tamanho = len(nome)
    return tamanho
