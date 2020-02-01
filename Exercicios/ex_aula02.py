#  _*_ coding: utf-8 _*_

# dados = {
#     'estados': {
#         'SP':{
#             'nome': 'São Paulo',
#             'municipios': 645,
#             'populacao': 44.04
#         },
#         'RJ':{
#             'nome': 'Rio de Janeiro',
#             'municipios': 92,
#             'populacao': 16.72
#         },
#         'MG':{
#             'nome': 'Minas Gerais',
#             'municipios': 31,
#             'populacao': 20.87
#         }
#     }
# }

# imprima as seguintes informações:

# 1= nome dos estados

# **** Eu fiz****

# print("Nome:",dados['estados']['SP']['nome'],",",dados['estados']['RJ']['nome'], ",",dados['estados']['MG']['nome'])

# Resultado /// Nome: São Paulo , Rio de Janeiro , Rio de Janeiro

# **** Renato fez**** 

# nome_sp = dados['estados']['SP']['nome']
# nome_rj = dados['estados']['RJ']['nome']
# nome_mg = dados['estados']['MG']['nome']

# print("Nome: {}".format(nome_sp))
# print("Nome: {}".format(nome_rj))
# print("Nome: {}".format(nome_mg))

# Resultado ///  
#  Nome: São Paulo
#  Nome: Rio de Janeiro
#  Nome: Minas Gerais



# # 2 - Nome dos estados e sua populações em milhões

# Formato:
# Nome: nome do estado, População: a quantidade

# nome_sp = dados['estados']['SP']['nome']
# nome_rj = dados['estados']['RJ']['nome']
# nome_mg = dados['estados']['MG']['nome']

# populacao_sp = dados['estados']['SP']['populacao']
# populacao_rj = dados['estados']['RJ']['populacao']
# populacao_mg = dados['estados']['MG']['populacao']

# print('Nome: {}\nPopulação:1{} Milhoes\n' .format(nome_sp, populacao_sp*100000))
# print('Nome: {}\nPopulação:1{} Milhoes\n' .format(nome_mg, populacao_mg*100000))
# print('Nome: {}\nPopulação:1{} Milhoes\n' .format(nome_rj, populacao_rj*100000))

# # // Resultado 

# Nome: São Paulo
# População:14404000.0 Milhoes

# Nome: Minas Gerais
# População:12087000.0 Milhoes

# Nome: Rio de Janeiro
# População:11672000.0 Milhoes




# # 3 - Nome dos estados e quantidade de municipios
# # Formato:
#  Nome: nome do estado, Muncipios: a quantidade 

# nome_sp = dados['estados']['SP']['nome']
# nome_rj = dados['estados']['RJ']['nome']
# nome_mg = dados['estados']['MG']['nome']

# mun_sp = dados['estados']['SP']['municipios']
# mun_rj = dados['estados']['RJ']['municipios']
# mun_mg = dados['estados']['MG']['municipios']

# print('Nome: {}\nQuantidade de Municipios:{}\n' .format(nome_sp, mun_sp))
# print('Nome: {}\nQuantidade de Municipios:{}\n' .format(nome_mg,mun_mg))
# print('Nome: {}\nQuantidade de Municipios:{}\n' .format(nome_rj,mun_rj))

# Nome: São Paulo
# Quantidade de Municipios:645

# Nome: Minas Gerais
# Quantidade de Municipios:31

# Nome: Rio de Janeiro
# Quantidade de Municipios:92

# ////////////////////////

# frutas = ['banana', 'abacaxi','maracuja']

# if 'caju' in frutas:
#     print('A Lista frutas não possui caju')
# else:
#     print("A Lista não possui Caju")

#     Resultado:

#   A Lista não possui Caju  

#///////////////////////////////

# usuarios = ['Rafael', 'Camila', 'Paulo', 'Pamela']

# var_usuarios = input("Digite o usuario:")

# if var_usuarios in usuarios:
#     print("Acesso Permitido")
# else:
#     print("Acesso Negado")