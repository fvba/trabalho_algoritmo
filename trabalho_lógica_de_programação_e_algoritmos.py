# -*- coding: utf-8 -*-
"""Trabalho Lógica de Programação e Algoritmos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gBPTFRKtYIwsKv-AoWJuyQMLA85nvzDm
"""

#Exercício 01

#Apresetação do Programa
nome_programa = 'Categoria por peso em esportes de luta' 
print('+',len(nome_programa)*'-','+')
print('|',nome_programa,'|')
print('+',len(nome_programa)*'-','+')

#Programa principal 
while True:
  nome = str (input('Informe o nome do lutador: ')) #Recebe o nome do lutador
  peso = float (input('Informe o peso do lutador: ')) #Recebe o peso do lutador

  #Faz a comparação e verifica a qual categoria de peso o lutador pertence:
  if peso < 65:
    categoria = 'Pena'
  elif 65 <= peso < 72:
    categoria = 'Leve'
  elif 72 <= peso < 79:
    categoria = 'Ligeiro'
  elif 79 <= peso < 86:
    categoria = 'Meio-médio'
  elif 86 <= peso < 93:
    categoria = 'Médio'
  elif 93 <= peso < 100:
    categoria = 'Meio-pesado'
  elif 100 <= peso:
    categoria = 'Pesado'

  #Apresenta os resultados:
  print('\nNome fornecido: {}' .format(nome)) 
  print('Peso fornecido: {}' .format(peso))
  print('O lutador {} pesa {} kg e se enquadra na categoria {}.\n' .format(nome,peso,categoria))
  
  #Faz a verificação se o usuário deseja continuar:
  sair = int (input('Deseja continuar? Escolha uma opção: (1 - Sim / 2 - Não): '))
  if sair == 2:
    print('Programa encerrado')
    break
  else:
    continue

#Exercício 02

#Esta função solicita que o usuário digite um código do tipo inteiro e verifica se ele está no intervalo correto
def valida_int (min,max): 
  while True:
    try: #Força o usuário a digitar um número inteiro
      codigo = int (input('Digite o código do produto vendido: '))
      break
    except ValueError: 
      print('Você não digitou um número inteiro, tente novamente...')
  if (codigo < min) or (codigo > max): #Faz a comparação e informa se o usuário digitou um código valido dentro do intervalo informado
    print('Você não digitou um código válido.')
  else:
    return codigo

#Eu decidi usar a cabeça e não utilizar soluções convencionais, partindo para a utilização de cálculos matemáticos
def descobrir_digito (cod): 

  z = cod #Recebe o código digitado pelo usuário

  c1 = z // 10000 #Calcula quantas unidades de 10000 exitem no código e descobre o prímeiro dígito do código informado pelo usuário
  m1 = c1 * 2 #Multiplica pelo dígito descoberto de acordo com a tabela informada no exercício
  z = z - c1*10000 #Retira do código as unidades de 10000 e consequentemente o primeiro dígito do código

  c2 = z // 1000 #Os cálculos a seguir repetem a mesma coisa para as unidades de 1000, 100, e 10
  m2 =  c2 * 3
  z = z - c2*1000

  c3 = z // 100
  m3 = c3 * 4
  z = z - c3*100

  c4 = z // 10
  m4 = c4 * 5
  z = z - c4*10

  m5 = z * 6

  #Após descobrir todos as multiplicações, encontra o total delas e calcula o resto por 7
  total = m1+m2+m3+m4+m5  
  res = total % 7
  return res

#Programa principal 
minimo = 10000
maximo = 30000
a = valida_int(minimo,maximo) #Faz a validação do código digitado pelo usuário
if a == None: #Se o código não for válido, informa para o usuário que o código deve respeitar certo intervalo
  print('Os códigos devem variar entre {} e {}.' .format(minimo,maximo))
else: #Se o cógido for válido, invoca a função que descobre o dígito e printa na tela o resultado
  dig = descobrir_digito(a)
  print('O código com dígito é {}-{}' .format(a,dig))

#Exercício 03

#Cria um dicionário vazio em que serão adicionadas informações ao longo do programa
alunos = {'nomes': [],'notas': [],'status':[]} 
#Cria as listas que serão adicionadas ao dicionário vazio
nomes = [] 
notas = []
status = []
#Solicita a quantidade de alunos que serão cadastrados
qt = int (input('Quantos alunos deseja cadastrar? ')) 

#Para a quantidade de alunos digitados, repetirá este laço:
for i in range (1,qt+1,1): 
  #Cria listas temporárias que serão adicionadas as listas definidas anteriormente 
  nomes_temp = [] 
  notas_temp = []
  status_temp = []

  #Solicita o nome do aluno e adiciona a lista temporária de nomes
  nome = str (input('\nDigite o nome do {}º aluno: ' .format(i))) 
  nomes_temp.append(nome)

  #Solicita as notas e adiciona a lista temporária de notas
  nota1 = float (input('Digite sua 1ª nota: ')) 
  nota2 = float (input('Digite sua 2ª nota: '))
  nota3 = float (input('Digite sua 3ª nota: '))
  nota4 = float (input('Digite sua 4ª nota: '))
  notas_temp.append(nota1)
  notas_temp.append(nota2)
  notas_temp.append(nota3)
  notas_temp.append(nota4)

  #Descobre se o aluno foi aprovado e adiciona a resposta a lista temporária de status
  media = (nota1 + nota2 + nota3 + nota4) / 4 
  if media >= 7:
    status_temp.append('Aprovado')
  else:
    status_temp.append('Reprovado')

  #Adiciona para as listas permanente as respostas sobre o aluno atual
  nomes.append(nomes_temp) 
  notas.append(notas_temp)
  status.append(status_temp)

#Adiciona as listas permantes ao dicionário
alunos['nomes'] = nomes 
alunos['notas'] = notas
alunos['status'] = status

#Exibe na tela a tabela (utilizando o dicionário criado no início) com o nome dos alunos, suas respectivas notas e o status
print('\nNotas dos alunos:') 
print('--------------------------------------------------')
print('Aluno | Nota 1 | Nota 2 | Nota 3 | Nota 4 | Status')
print('--------------------------------------------------')
for i in range (0,qt):
  print('{} | {} | {} | {} | {} | {}' .format(alunos['nomes'][i][0], alunos['notas'][i][0], alunos['notas'][i][1], alunos['notas'][i][2], alunos['notas'][i][3], alunos['status'][i][0]))

#Exercício 04

#Cria uma lista para cada tipo de dado
nomes = [] 
idades = []
telefones = []

#Apresenta o programa e as instruções para utilizá-lo
print('+------------------------------+') 
print('|Cadastro de Agenda Telefônica |')
print('+------------------------------+')
print('|Instruções:                   |')
print('|Cadastre nome, idade e telefo-|')
print('|ne. Para encerrar, não digite |')
print('|nada no nome e aperte a tecla |')
print('|enter.                        |')
print('+------------------------------+')

#Recebe os dados e verifica se deve continuar o cadastro ou não (string vazia)
#Cria um Contador para saber quantas pessoas foram cadastradas na agenda
contador = 0 
while True: 
  nome = str (input('\nDigite o nome do contato: '))
  if nome == '':
    break
  else:
    idade = int (input('Digite a idade do contato: '))
    telefone = int (input('Digite o número de telefone do contato: '))
    nomes.append(nome)
    idades.append(idade)
    telefones.append(telefone)
    contador += 1

#Cria lista que receberá os dados agrupados de forma compatível (nome - idade - telefone) e posteriormente será ordenada em ordem alfabética
lista_ordenada = [] 

#Agrupa os dados em uma lista temporária e depois adiciona esta lista temporária a lista que será ordenada em ordem alfabética
for i in range (0,contador): 
  lista_temp = []
  lista_temp.append(nomes[i])
  lista_temp.append(idades[i])
  lista_temp.append(telefones[i])
  lista_ordenada.append(lista_temp)

#Ordena a lista para ordem alfabética
lista_ordenada.sort() 

#Exibe os dados da agenda em ordem alfabética utilizando a lista ordenada
print('\nLista de contato em ordem alfabética:') 
print('-------------------------------------')
print('   Nome   |   Idade   |   Telefone   ')
print('-------------------------------------')
for i in range (0,contador):
  print('{} |   {}   |   {}   ' .format(lista_ordenada[i][0], lista_ordenada[i][1], lista_ordenada[i][2]))

#Eliminando a lista conforme os dados vão sendo adicionados ao dicionário

#Cria listas temporárias que serão adicionadas a um dicionário
nomes_menores = [] 
idades_menores = []
telefones_menores = []

nomes_maiores = []
idades_maiores = []
telefones_maiores = []

#Adiciona os elemento às listas temporárias conforme a idade
#Deleta os dados conforme eles vão sendo adicionados às listas temporárias, conforme solicitado no exercício
x=0
while x < contador:
  if lista_ordenada[0][1] >= 18:
    nomes_maiores.append(lista_ordenada[0][0])
    idades_maiores.append(lista_ordenada[0][1])
    telefones_maiores.append(lista_ordenada[0][2])
    del(lista_ordenada[0])
  else:
    nomes_menores.append(lista_ordenada[0][0])
    idades_menores.append(lista_ordenada[0][1])
    telefones_menores.append(lista_ordenada[0][2])
    del(lista_ordenada[0])
  x += 1

#Adiciona os dados das listas temporárias ao dicionário que será exibido na tela
menor_18 = {'nomes': nomes_menores,'idades': idades_menores,'telefones': telefones_menores}
maior_18 = {'nomes': nomes_maiores,'idades': idades_maiores,'telefones': telefones_maiores}

#Deleta as listas temporárias
del(nomes_menores,idades_menores,telefones_menores)
del(nomes_maiores,idades_maiores,telefones_maiores)

#Exibe os dicioários conforme o critério de idade
print('\nDicionário com os contatos de acordo com a idade:')
print('-----------------------------------------------------')
print('Dicionário com os contatos menores de 18 anos:')
print(menor_18)
print('-----------------------------------------------------')
print('Dicionário com os contatos maiores ou iguais a 18 anos')
print(maior_18)