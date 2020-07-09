def menu():
    print('\033[33;1m||||||||SISTEMA ESCOLAR||||||||\033[m')
a7 = ['mateus aviz', 'luis eduardo', 'marcos andrade', 'janaina correa', 'marcelo sampaio', 'paulo silva', 'maria de jesus', 'cassio furtado', 'thiago andradade', 'endrio correa', 'luis sousa']
b7 = ['maria andrade', 'lucas matos', 'marcela correa', 'tiago lenine', 'andersson marques', 'cassiano vale', 'lucio vale', 'caio neto']
a7.sort()
b7.sort()
n = 0
menu()
escolha = input('\033[30;3mdigite a sala:\033[m ').upper().strip()
if escolha == 'A7':
    while n < len(a7):
        print('\033[30mALUNO:\033[m \033[31;1m{:>24}\033[m'.format(a7[n]))
        n = n + 1
    resp = input('Deseja buscar sobre algum aluno (s/n): ').lower().strip()
    if resp == 's':
        n = 0
        aluno = input('digite o nome do aluno: ').lower().strip()
        if aluno in a7:
            while aluno != a7[n]:
                n = n + 1
        print('O numero do aluno é \033[33m{}\033[m'.format(n + 1))
elif escolha == 'B7':
    while n < len(b7):
        print('\033[30mALUNO:\033[m \033[31m{}\033[m'.format(b7[n]))
        n = n + 1
    resp = input('Deseja buscar sobre algum aluno (s/n): ').lower().strip()
    if resp == 's':
        n = 0
        aluno = input('digite o nome do aluno: ').lower().strip()
        while aluno != b7[n]:
            n = n + 1
        print('O numero do aluno é \033[33m{}\033[m'.format(n + 1))
else:
    print('\033[31mNão está no sistema ou erro de digitação!\033[m')
menu()
