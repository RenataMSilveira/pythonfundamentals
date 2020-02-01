# _*_ coding: utf-8 _*_

# var = input('Digite o Valor')


# texto = ' esse é um texto'

# texto.upper - 'Maiuscula'
# texto.lower - 'minuscula'
# texto.capitalize - 'primeira Maiuscula'
# texto.split - ('') insere virgula entre o texto digitado

#***********************************************************************

# lista = ['abacaxi', 'banana','navio',15,5.5]
# print(lista[3]) - mostra o item da lista

# lista.append
# lista.pop (0) apaga o item da posição informada
# lista.remove ('abacaxi')apaga o item escrito
# lista.sort()

#*********************************************************

# lista = ['1','2','3','4']

# tupla = (1,2,3,4,5) não permite alteração de valores, somente se a variável for declarada novamente.

# Exemplos :

# ** lista ** lista= [1,2,3,(4,5,7),'teste']
# **tupla** valores = (1,2,3,4 [1,2,3],{'chave': 'valor'})

#**********************************************************

# # Dicionarios

# ling_favorita = { 'Joao':'Java', 'Daniel': 'Python', 'Hector':'PHP'}

# print(ling_favorita['Daniel'])

#*************************************************

# time_favorito = {'Joao':'Corinthians', 'Paula':'Santos', 'Camila':'Palmeiras'}

# # print(time_favorito['Paula'])


# # time_favorito.update({'Paula':'Flamengo'})

# # print(time_favorito.values())
# # print(time_favorito.keys())

# time_favorito['Joao'] = time_favorito['Camila']

# print(time_favorito)

#-----------------------

# dados_clientes = {'cliente': {'cl001': {'nome': 'Rafael da silva','idade': 25,'telefone': '011954243647'},
#                               'cl002': {'nome': 'Carla Pereira','idade': 28,'telefone': ''}}}


# # print(dados_clientes['cliente']['cl002']['nome'])

# # *********** Inserir/alterar dados: *******************

# dados_clientes['cliente']['cl002']['telefone']= '12333444567'

# #************ Mostrar Dados*****************************

# # print(dados_clientes['cliente']['cl002'])

# # ///////////////////////////////////////////////

# imprime_clientename = input("Digite o código do cliente")

# print(dados_clientes ['cliente'][imprime_clientename])


# ////************** If e Else*****************

# idade = int(input('Digite sua Idade:'))

# habilitacao = int(input('Possui habilitação:\n 1- para sim\n 2- para não\n>'))

# if idade >= 18 and habilitacao == 1:
#     print ('Você pode Beber')

# else:
#     print ('Você não pode Beber')

# #***Resultado 

# Digite sua Idade:30
# Possui habilitação:
#  1- para sim
#  2- para não
# >1
# Você pode Beber
      