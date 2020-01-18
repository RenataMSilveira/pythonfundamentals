Tipos de Dados
 '''
 doc string
'''

print('Curso Python Fundamentals')
print (100)
print (1.5)

 usuario = input ("Digite Seu Nome:")
 print(usuario)

 n1 = int(input("Digite o Primeiro Número: "))
 n2 = int(input("Digite o Segundo Número: "))

 print (n1 + n2)

 print ("Programa de Notas")

 print ("Informe as notas abaixo:" )
 n1 = float(input ("Nota 1:"))
 n2 = float(input ("Nota 2:"))
 n3 = float(input ("Nota 3:"))
 n4 = float(input ("Nota 4:"))

media = (n1 + n2 + n3 + n4)/4

print("Média:")
 print (media)



lista = ['Corinthians', [1, 2, 3, 4, 5], 'Palmeiras', 'São Paulo', [10, 11, 12, 13, 14],'Flamengo', 'Vasco']

print(lista[1][2], lista[4][3], lista[6])

print(lista[1][3], lista[3], lista[4][4])

'''
print 4, São Paulo, 14
'''

print(lista[0], lista[1][1], lista[4][0], lista[4][4])

'''
print Corinthians, 2, 10, 14
'''