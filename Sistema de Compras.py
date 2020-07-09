print('\033[46m                                                  \033[m')
print('\033[3;1;33m               SISTEMA DE COMPRAS                 \033[m')
lista = [3.00, 4.50, 2.90, 5.00, 5.00]#Preços dos produtos em ordem de lista
PRODUTOS = ['Café', 'Açúcar', 'Arroz', 'Refrigerante', 'Leite']
codigo = [1, 2, 3, 4, 5]#lista para corresponder ao codigo que representa o produto
n = 0
resp2 = 'n'
#INICIO DO ALGORITMO
print('\033[30m-------------------PRODUTOS-----------------------\033[m')
# 1 - Exibe os produtos disponíveis e os respectivos preços
while n < len(PRODUTOS):#repete
    print('\033[31m{:20}\033[m \033[30m{:.2f} R$\033[m  \033[33mCódigo do produto:\033[m \033[30m{}\033[m'.format(PRODUTOS[n], lista[n], n + 1))
    n = n + 1 #contador
#Trecho que cuida da escolha do usuário
finalpreco = 0
while resp2 == 'n':
    escolha = int(input('Entre com  a opção: '))
    n = 0
    while escolha != codigo[n]:
        n = n + 1
    resp = PRODUTOS[n]
    finalpreco = finalpreco + lista[n]
    print('O produto selecionado: \033[31m{}\033[m | Preço: \033[31m{:.2f}\033[m'.format(resp, lista[n]))
    resp2 = str(input('Quer encerrar o processo (s) (n): '))
print('VALOR TOTAL A PAGAR \033[31m{:.2f} R$\033[m '.format(finalpreco))
print('\033[40m  \033[m   \033[41m  \033[m   \033[42m  \033[m   \033[43m  \033[m  \033[44m  \033[m')#blocos de cores
print('\033[31m||||||||FIM DO PROGRAMA|||||||\033[m')
print('\033[46m                                                  \033[m')
