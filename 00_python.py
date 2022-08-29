#!/usr/bin/env python
# coding: utf-8

# Variáveis

# **Geral**</br>
# Variáveis são utilizadas para armazenar valores dentro do código, existem diferentes tipos de variáveis, cada uma adequada para alguma situação
# >> **Alguns dos tipos primários de variáveis**
# **int**: utilizadas para armazenar números inteiros. </br>
# **float**:utilizada para pontos flutuantes, ou seja, números reais. <br>
# **string**: utilizada para armazenar textos. <br>
# **boleaano**: utilizada para armazenar condição binária de True ou False
# 
# Em Python não precisamos declarar o tipo de variável, ele reconhece de forma automática
# 
# <h1> Exemplos: </h1>
# 


inteiro = 1
real = 3.45
texto = 'isso é uma string'
texto_2 = "isso também, pode escolher aspas simples ou duplas"
booleano = True


# Para saber o valor da variável podemos colocar a função print, como no exemplo abaixo:

# In[ ]:


#podemos colocar comentários dentro de uma célula de código dessa forma
print(real)


# In[ ]:


#podemos colocar diversos prints na mesma célula
print(inteiro)
print(real)
print(texto)
print(texto_2)
print(booleano)


# In[ ]:


#ou podemos imprimir tudo em uma única linha
print(inteiro,real,texto,texto_2,booleano)


# In[ ]:


#podemos também usar uma linha de código e printar pulando linha com o \n
print(inteiro,'\n',real,'\n',texto,'\n',texto_2,'\n',booleano)


# Como em nenhum momento é declarado o tipo da variável e o python reconhece sozinho, verificar se o tipo da variável foi reconhecido corretamente é uma boa prática e ajuda diagnosticar muitos erros de código.

# In[ ]:


#o python possui a função "type()" já nativa e construída para mostar o tipo da variável
print('Inteiro:',inteiro, ' Tipo:',type(inteiro))
print('Real:',real, ' Tipo:',type(real))
print('Texto:',texto, ' Tipo:',type(texto))
print('texto_2:',texto_2, ' Tipo:',type(texto_2))
print('Booleano:',booleano, ' Tipo:',type(booleano))


# <b><h2>Dicas</h2>

# O Python é case sensitive, ou seja, caso você colocar a mesma letra maiúscula onde é minúscula ele não vai reconhecer.

# In[ ]:


print(Inteiro) # Sempre bom ter cuidado quanto a digitação
# print(inteiro) é o certo por conta do "i" minísculo


# Sempre deixe o código em ordem de execução e atribua sempre nomes autoexplicativos para as variáveis, sempre vai te ajudar saber qual valor está ali e ajudará na hora de utilizar.

# <h1>Exercícios:<h1>

# 1. Na célula abaixo crie uma variável de cada tipo aprendido e atribua um valor para cada uma delas, lembre-se de utilizar as dicas da aula.

# In[ ]:


number_1 = 10 #um numero qualquer sem "."e sem estar dentro de '' ou ""
number_2 = 10.5 #um numero qualquer com o "." e sem estar dentro de '' ou ""
text = "Hello World" #qualquer caracter dentro de aspas simples ou duplas
bool = False


# 2. Na célula abaixo imprima os valores atribuídos em cada variável, pula uma linha de uma variável para a outra.

# In[ ]:


print (number_1,'\n',number_2,'\n',text,'\n',bool)


# 3. Na Célula abaixo imprima os tipos de cada variável.

# In[ ]:


print (type(number_1)) 
print (type(number_2)) 
print (type(text))
print (type(bool))


# <h3> Definições</h3>
# 
# Na linguagem de programação é feito a manipulação de variáveis. Traremos as definições como material de apoio à aula: 
# 
# **Variável** <br>
# - É o nome que se refere a um valor, um endereço simbólico; </br>
# - Pode assumir valores distintos, mas somente um único valor a cada instante da execução do programa/algoritmo.  
# - **Comando de atribuição** Criam uma nova variável e também fornecem a elas o valor ao qual varão referência
# 
# **Tipos de Variáveis**
# - Os valores e variáveis em Python são classificados em diferentes tipos que definem os valores que a variável pode assumir e quais operações que podem ser realizadas. 
# - O tipo da variável se altera conforme o dado armazenado. 
# - Comando *type(x)* - permite saber o tipo do valor ou variável em x. 

# # Operações

# 
# <h1> Operações </h1>
# <h2> Relembrando um pouco de variáveis </h2>
# <b> Geral:</b><br>
# Variáveis são utilizadas para armazenar valores dentro do código, existem diferentes tipos de variáveis, cada uma adequada para alguma situação.
# <br> <br>
# 
# > <b> Alguns dos tipos primários de variáveis</b><br>
# <b>int:</b> utilizadas para armazenar números inteiros.<br>
# <b>float:</b> utilizada para pontos flutuantes, ou seja, números reais.<br>
# <b>string:</b> utilizadas para armazenar textos. <br>
# <b>boleeano:</b> utilizadas para armazenar condição binária de True (verdadeiro) ou False (falso). <br>
# <br>
# 
# 
# 
# 
# Em python não precisamos declarar o tipo de variável, ele reconhece de forma automática.<br>
# 
# <h1> Operações</h1>
# 
# Principais operações em python são:
# 
# *   <b>Soma:</b> para operações de soma é utilizado o sinal de +
# *   <b>Subtração:</b> para operações de subtração é utilizado o sinal de -
# *   <b>Multiplicação:</b> para operações de Multiplicação é utilizado o sinal de *
# *   <b>Divisão:</b> para operações de divisão é utilizado o sinal de /
# 
# <h2> Exemplos:</h2>
# 
# 
# 

# In[ ]:


#soma de inteiros no print
inteiro_1 = 5
inteiro_2 = 7
#print dos inteiros + strings descrevendo operação
print('somando:',inteiro_1, '+', inteiro_2,'=',inteiro_1 + inteiro_2)


# In[ ]:


#soma de strings no print
texto = 'oi'
texto_2 = "tchau"
print('Somando:',texto, '+', texto_2,'=',texto + texto_2)


# In[ ]:


# E também multiplicar uma string por um inteiro no print
print('Multiplicando:',texto*3 )


# Podemos também atribuir os valores das operações em uma nova variável ou atribuir como o novo valor da variável já existente.

# In[ ]:


#somando dois inteiros e atribuindo a uma nova variável
inteiro_3 = inteiro_1 + inteiro_2
#printando a váriavel e seu type
print(inteiro_3, type(inteiro_3))


# In[ ]:


#somando um inteiros e um número real e atribuindo a uma nova variável
inteiro_3 = inteiro_1 + real_1
#printando a váriavel e seu type
print(inteiro_3, type(inteiro_3))


# Ao realizar operações o tipo da nossa variável pode mudar.

# Existem também operadores que os resultados são booleanos, esses operadores são voltados para comparação
# 
# *   Maior > Menor 
# *   Igual: ==
# *   Diferente: !=

# In[ ]:


#printando comparações entre 2 valores com cada um dos operadores
print(5>3)
print(5<3)
print(7==7)
print(7==7.5)
print(7!=7)


# Por trás do operador booleano existe o 0 para False e o 1 para True, logo se realizarmos uma soma o resultado será o seguinte

# In[ ]:


#somando valores booleanos True
True + True


# In[ ]:


#somando true com false
True+False


# In[ ]:


#multiplicando true
True*3


# In[ ]:


#dividindo true e atribuindo a uma nova variavel
booleano = True/2
#printando o valor da variável e seu type
print(booleano,type(booleano))


# O Python também fornece funções built in (nativas) que permitem você transformar o valor de uma variável.

# In[ ]:


#o python possui a função "type()" já nativa e construída para mostar o tipo da variável
print('Booleano:',booleano, ' Tipo:',type(booleano))
#convertendo variável booleano para int
booleano = int(booleano)
#printando variável e seu type
print('Booleano:',booleano, ' Tipo:',type(booleano))
#convertendo o valor para string
booleano = str(booleano)
#printando variável e seu type
print('Booleano:',booleano, ' Tipo:',type(booleano))


# # Operações 2

# Além das operações mais comuns, o Python nativamente oferece operações de:
# 
# *   <b>Módulo: </b> %
# *   <b>Exponencial: </b> **
# *   <b>Divisão com arredondamento: </b> //
# 
# <h2> Exemplos </h2>

# In[ ]:


#basicamente a sobra da divisão
#Muito utilizado para verificar se um número é par, caso o resto da divisão por 2 for 0, ele é par
print(9%2)
print(4%2)


# In[ ]:


#Printando operação de 2 numeros com Exponencial
print(2 ** 2)
print('o mesmo que: ',2*2)
print(1.3 **3)
print('O mesmo que: ',1.3*1.3*1.3)


# In[ ]:


#Divisão com arredondamento
print(5//2)
print(5//3)
print(5//4)


# In[ ]:


#Divisão com arredondamento
var_arredondamento = 21//4
print (var_arredondamento, type (var_arredondamento))


# <h2> Dicas </h2>

# Um dos grandes motivos do Python ter conseguido tanto espaço é a constante atualização para deixar cada vez mais acessível, rápido e fácil codificar, então as operações visto acima podem ser feitas da seguinte forma:

# In[ ]:


x = 1
y = 1
x+=10
y+=10
print('x:',x,'y:',y)
print("x += 10 é equivalente a: x = x + 10")


# <h1>Exercícios:<h1>

# 1. Faça pelo menos 1 exemplo com cada operador visto utilizando variáveis do mesmo tipo.

# In[ ]:


inteiro1 = 5
inteiro2 = 6

print(inteiro1/ inteiro2)
print(inteiro1 // inteiro2)
print(inteiro1 % inteiro2)
print(inteiro1 * inteiro2)
print(inteiro1 ** inteiro2)
print(inteiro1 + inteiro2)
print(inteiro1 - inteiro2)
print(inteiro1 > inteiro2)
print(inteiro1 < inteiro2)
print(inteiro1 == inteiro2)
print(inteiro1 != inteiro2)


# 2. Repita o exercício 1 mas dessa vez utilizando variáveis de tipos diferentes, dessa vez verifique se o tipo dela alterou ou não.

# In[ ]:


inteiro1 = 9
inteiro2 = 3.9
print(inteiro1/ inteiro2)
print(inteiro1 // inteiro2)
print(inteiro1 % inteiro2)
print(inteiro1 * inteiro2)
print(inteiro1 ** inteiro2)
print(inteiro1 + inteiro2)
print(inteiro1 - inteiro2)
print(inteiro1 > inteiro2)
print(inteiro1 < inteiro2)
print(inteiro1 == inteiro2)
print(inteiro1 != inteiro2)


# 
# 3. Faça 3 operações com operadores diferentes utilizando o formato passado na em Dicas.
# 

# In[ ]:


print(inteiro1)
inteiro1+1
print(inteiro1)
inteiro1-1
print(inteiro1)
inteiro1*=2
print(inteiro1)
inteiro1/=2
print(inteiro1)


# # <h1>  Condicionais </h1>

# 
# 
# <h2> Relembrando um pouco de operações </h2>
# <b> Geral:</b><br>
# Toda condicional em um código depende do resultado de uma operação booleana.
# <br> <br>
# 
# > <b> As principais condições utilizadas são:</b><br>
# <b>==:</b> Verifica se os valores são exatamente iguais.<br>
# <b>>:</b> Verifica se o valor a esquerda é maior do que o valor a esquerda.<br>
# <b><:</b> Verifica se o valor a esquerda é menor do que o valor a esquerda. <br>
# <b>>=:</b> Verifica se o alor a esquerda é maior ou igual comparado ao valor a esquerda. <br>
# <b><=:</b> Verifica se o valor a esquerda é menor ou igual comparado ao valor a esquerda. <br>
# <b>in:</b> Verifica se os a esquerda está contido no valor a direita. <br>
# <br>
# 
# 
# 
# 
# 

#  **As condicionais em python são declaradas utilizando a sintaxe abaixo:**<br> 
# 
# <b>if x == y:</b> *Compara se x e y são iguais*<br>
# <b>elif x > y:</b> *Caso x e y seja diferente compara se x é menor que y*<br>
# <b>else:</b> *Caso nenhuma condição acima seja verdade ele executa esse bloco.*
# 
# 

# In[ ]:


#é possível também fazer uma operação antes do x e fazer a verificação com o seu resultado.
x=4
if x%2==0:
  print("x é par")
else:
  print("x é ímpar")


# In[ ]:


#caso tenha mais de uma condição para validar é utilizado o elif como um else+if
#print verdadeiro no else
x = 5
y = 10
if x == y:
  print("são iguais")
elif x > y:
  print("x é maior que y")
else:
  print("são diferentes e x não é maior que y")


# In[ ]:


#print verdadeiro no elif
x = 5.5
y = 5
if x == y:
  print("são iguais")
elif x > y:
  print("x é maior que y")
else:
  print("são diferentes e x não é maior que y")


# In[ ]:


#print verdadeiro no if
x = 5
y = 5
if x == y:
  print("são iguais")
elif x > y:
  print("x é maior que y")
else:
  print("são diferentes e x não é maior que y")


# <h1> Dois novos tipos de váriaveis</h1>
# 
# Nessa etapa vamos aprender mais dois tipos de váriaveis, até essa etapa já vimos string, inteiros, booleanas e números reais, mas e se quisermos armazenar diversos valores? Temos que declarar diversas variáveis? Para esses casos podemos a Lista e a Tupla, ambas são para armazenar diversos valores em uma única variável.
# 
# *   <b>Lista:</b> varíavel mutável que armazena diversos valores heterogêneos ou homogêneos
# *   <b>Tupla:</b> varíavel imutável que armazena diversos valores heterogêneos ou homogêneos.
# 
# A grande diferença entre as duas é que a lista permite alterar valores dentro dela enquanto a tupla não permite alterações.
# 
# <h2> Exemplos:</h2>
# 

# É possível também fazer operações entre strings.

# In[ ]:


#criação de lista e tupla com valores de diferentes tipos
lista = ['oi',5,'tchau']
tupla = ('oi',5,'tchau')
#por mais que contenham os mesmos valores, são tipos diferentes e isso torna elas diferentes
lista==tupla


# In[ ]:


#print do primeiro valor da lista e da tupla
print(lista[0])
print(tupla[0])
#quanto comparamos o valor podemos ver que é igual
lista[0]==tupla[0]


# Podemos adicionar, remover ou alterar valores da lista, enquanto a tupla não permite essas ações por ser imutável.

# In[ ]:


#adição de um elemento na lista
lista.append('ultimo')
#print da lista
print(lista)
#atribuindo um novo valor ao último elemento da lista
lista[-1]='alterado'
#print da lista
print(lista)
#remoção (pop) do último elemento da lista
lista.pop(-1)
print(lista)


# É possível converter a tupla em lista para adicionar valores.

# In[ ]:


#convertendo tupla em lista
tupla = list(tupla)
#adicionando um valor ao final da tupla
tupla.append('adicionado')
#printando a tupla e seu type
print(tupla,type(tupla))


# Verificando valores dentro de uma lista
# 
# 

# In[ ]:


#verificando se "oi" está na lista
if 'oi' in lista:
  print('oi está na lista')


# In[ ]:


#verificando se "ei" está na lista
if 'ei' in lista:
  print('ei está na lista')
else:
  print('ei não está na lista')


# Podemos também utilizar as expressões and e or para colocar duas ou mais condições dentro da mesma linha do if

# In[ ]:


#verificando se x ESTÁ NA lista E x maior > que 3 E x < menor que 10
x=5
if x in lista and x>3 and x<10:
  print("x está na lista, é maior que 3 e menor do que 10")


# In[ ]:


#verificando se x NÃO ESTÁ na lista OU x maior > que 3 E x < menor que 10
x=5
if x not in lista or x>3 and x<10:
  print("ou x não está na lista ou é maior que 3 e menor do que 10")


# Nas aulas e exercícios adiantes aprenderemos cada vez mais novos conceitos na medida que nos aprofundamos no que já vimos. É recomendado que seja feito todos os exercícios e pontuado cada dúvida que surgir.

# <h2> Dicas </h2>

# 
# 
# > O python nos dá uma série de opções para resolver o mesmo problema, cabe a nós decidir qual é o mais adequado para cada situação. Tuplas e listas são ótimos exemplos disso, ambos podem resolver o problema de armazenar diversos valores em uma única variável, entretanto um é mutável e a outra não, cabe analisarmos a situação e ver qual melhor atende a necessidade. <br> <br>Caso você queira saber mais sobre quando usar qual tipo e quais as suas particularidades, esse [link](https://pt.stackoverflow.com/questions/192727/quando-usar-listas-e-quando-usar-tuplas#:~:text=As%20tuplas%20s%C3%A3o%20sequ%C3%AAncias%20imut%C3%A1veis,armazenamento%20em%20set%20ou%20dict%20).) no StackOverflow (se você ainda não conhece essa plataforma, é uma ótima oportunidade de conhecer, no decorrer do curso e da sua nova carreira, ela será sua grande companheira) vai te ajudar bastante.
# 
# 

# In[ ]:


x = 1
y = 1
x+=10
y+=10
print('x:',x,'y:',y)
print("x += 10 é equivalente a: x = x + 10")


# <h1>Exercícios:<h1>

# 1. Construa uma condição para verificar se o número é múltiplo de 3.

# In[ ]:


inteiro = 9
if inteiro %3==0:
  print('É múltuplo de 3') 


# 2. Crie 3 condicionais utilizando a estrutura elif.

# In[ ]:


inteiro = 11
if inteiro %3==0:
  print('É múltiplo de 3')
elif inteiro %4==0:
  print('é multiplo de 4')
elif inteiro %2 ==0:
  print('é par')
else: #else não permite condição (>/</=/...) 
  print('é ímpar')


# 
# 3. Crie uma lista e verifique se ela contém os números 7 e 3.
# 

# In[ ]:


lista = [1,2,3,4,2,4,7,6,5,3,7]
if 7 in lista and 3 in lista:
  print('contém 3 e 7')
elif 3 in lista:
  print('contém 3')
elif 7 in lista:
  print('contém 7')
else:
  print('não contém nem 3 e nem 7')


# <h1>Desafio:<h1>

# Crie uma lista com 5 valores e uma tupla com 10 valores, verifique se algum valor da lista está contido na tupla.

# In[ ]:


lista = [77, 2,3,4,5]
tupla = [3,2,4,2,5,2,1,3,2,7]
if lista[0] in tupla:
  print(lista[0], 'contém na tupla')
if lista[1] in tupla:
  print(lista[1], 'contém na tupla')
if lista[2] in tupla:
  print(lista[2], 'contém na tupla')
if lista[3] in tupla:
  print(lista[3], 'contém na tupla')
if lista[4] in tupla:
  print(lista[4], 'contém na tupla')


# In[ ]:


# Minha versão  
list = [0, 1, 3, 6, 7]
tuple = (0, 1, 3, 6 ,7, 8, 10, 14, 37, 19.2)

[list for item in [0, 1, 3, 6, 7] if 1 in tuple]
print ('tem sim')


# # <h1>Loop</h1>

# 
# 
# <b> Geral:</b><br>
# Loop é uma estrutura de repetição, onde o bloco de código dentro dessa estrutura executa os comandos até a condição do Loop ser False.
# <br> <br>
# 
# >Essa nova função nos ajudará resolver o desafio da tarefa anterior de forma mais eficiente e contínua. Para quem não conhece essa estrutura, a prática é essencial para absorver seu funcionamento.
# 
# 
# 
# 

#  Existem duas principais estruturas para criação de Loops, sendo elas:<br> 
# 
# <b>For:</b> *bloco menor e mais utilizado em python*<br>
# <b>While:</b> *bloco maior, utilizado mais em casos específicos*<br>
# 
# 
# 

# <h2> Comentários do Mumu </h2> 
# </br> O <b>for</b> é utilizado para loopings infinitos. </br>
# Já o <b>While</b> é usado para loopings até determinado valor.  

# In[ ]:


# a estrutura while tem funcionamento parecido com o for mas com sintaxe um pouco maior
#para um bloco executar 10x
contador = 0
while contador <5:
  print(contador)
  contador+=1


# In[ ]:


#mesmo código acima com for
for a in range(10):
  print(a)


# In[ ]:


#executando loop enquanto x é menor que y
x=10
y=20
while x < y:
  x=x+3
  y=y+1
  print(x,y)


# In[ ]:


#percorrendo uma lista com for
lista=['oi',7,'15',22,33.5]
for a in lista:
  print(a)


# In[ ]:


#resolvendo o desafio aula anterior
tupla=(1,2,3,4,5,6,7,8,9,10)
for a in lista:
  if a in tupla:
    print(a,' tem na tupla')


# In[ ]:


#é possível parar o comando for assim que encontrar o item desejado utilizando o break
for a in lista:
  if type(a)==int:
    print(a,' = inteiro encontrado')
    break


# In[ ]:


#percorrendo a lista e printando o type de cada váriavel se estiverem nas condicionais
for a in lista:
  if type(a)==int:
    print(a,'= inteiro')
  elif type(a)==str:
    print(a,'= string')
  elif type(a)==float:
    print(a,'= float')
  else:
    print('tipo nao listado')


# In[ ]:


#criando uma lista com range até 100
lista_2 = []
for a in range(100):
  lista_2.append(a)
lista_2


# <h1>Exercícios:<h1>

# 1. Crie uma lista contendo os números pares de 0 até 1000

# In[ ]:


lista = []
for a in range (0,1000,2):
    lista.append(a)
lista


# 2. Transforme cada valor da lista anterior em um string.

# In[ ]:


lista2 = []
for a in lista:
  lista2.append(str(a))
lista2


# 3. Compare os valores entre as listas e some os valores das 2 listas.

# In[ ]:


#Ou seja, some dois tipos de variáveis diferentes (str e int)
for a in lista:
  if a in lista2:
    print(a, 'contém na lista')
  else:
    print(a, 'não contém na lista')


# 4. Crie um *for* para reproduzir a [sequência de Fibonacci](https://www.coc.com.br/blog/soualuno/matematica/o-que-e-a-sequencia-de-fibonacci#:~:text=A%20sequ%C3%AAncia%20de%20Fibonacci%20%C3%A9,no%20final%20do%20s%C3%A9culo%2012.&text=Desde%20que%20nenhum%20coelho%20morra,os%20n%C3%BAmeros%200%20e%201.).

# In[ ]:


x = 0
y = 1
for a in range(10):
  print(x)
  b = x+y
  x=y
  y=b


# In[ ]:


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
nterms = 10
# check if the number of terms is valid
if nterms <= 0:
   print("Plese enter a positive integer")
else:
   print("Sequencia Fibonacci:")
   for i in range(nterms):
       print(recur_fibo(i), end ="") #


# 4.1. Crie um *While* para reproduzir a sequência de Fibonacci

# In[ ]:


n = int(input("Que termo deseja encontrar:"))
ultimo=1
penultimo=1

if (n==1) or (n==2):
    print("1")
else:
    count=3
    while count <= n:
        termo = ultimo + penultimo
        penultimo = ultimo
        ultimo = termo
        count += 1
    print(termo)


# 5. Crie um for que execute até aparecer a palavra "parar".

# In[ ]:


palavras=['continue','ok','segue','opa,','quase','parar',':)']
while a !="parar":
  a = input() #código para permitir o usuário digitar


# <h1> Loop 2</h1>
# 
# Nessa aula vamos aprender utilizar o Loop com algumas funções novas.
# 
# *   <b>Enumerate:</b> função para enumerar cada iteração.
# *   <b>Zip:</b> Agrupa duas ou mais iteções simultâneas.
# 
# 
# 
# <h2> Exemplos:</h2>
# 

# In[ ]:


#criando uma lista e percorrendo ela no for com enumerate printando a e b
lista = ['oi',5,'tchau',10]
for a,b in enumerate(lista):
  print(a,b)


# In[ ]:


#criando uma tupla e percorrendo ela e a lista com zip printando os 2 valores
tupla = ('oi',5,'tchau',20)

for a,b in zip(lista, tupla):
  print(a,b)


# In[ ]:


#é possível começar o range de outro ponto que não o 0
for a in range(2,10):
  print(a)


# In[ ]:


#e também ir somando mais de +1 por repetição do for
for a in range(3,21,3):
  print(a)


# In[ ]:


#podemos utilizar o else no for diretamente sem o if
for a in range(5):
  print(a)
else:
  print('próximo número passou do range')


# In[ ]:


#percorrendo uma string com o for
texto = 'vou fazer todos os exercícios'
for a in texto:
  print(a)


# In[ ]:


#atribuindo o split da string a uma nova variável e printando o resultado 
texto_2=texto.split()
texto_2


# In[ ]:


# Pegando palavra por palavra
for a in texto_2:
  print(a)


# In[ ]:


#deixando a primeira letra de cada palavra maiúscula
for a in texto_2:
  print(a[0].upper()+a[1:])


# In[ ]:


#for aninhado percorrendo a lista
for a in texto_2:
  for b in texto_2:
    print(a,b)


# In[ ]:


#for aninhado printando uma tabuada
for a in range(10):
  for b in range(10):
    print(a,' x ',b,' = ',a*b)


# <h1>Exercícios:<h1>

# 1. Crie um Loop que percorra uma string e coloque a posição de cada caracter contida nela.

# In[ ]:


texto = "Será que a Marina tá olhando meu código?"
for a in enumerate(texto):
  print(a)


# 2. Refaça o exercício 1 mas dessa vez pulando os espaços.

# In[ ]:


for a in enumerate(texto.replace(" ", "")):
  print(a)


# In[ ]:


for a,b in enumerate(texto):
  if b !=" ":
    print(a,b)


# 3. crie duas listas e percorra as duas no mesmo for, se elas tiverem tamanhos diferentes descreva o que acontece.

# In[ ]:


lista_1 = [35, 33, 47, 98, 69]
lista_2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for a,b in zip(lista_1, lista_2):
  print(a,b)
#É percorrido até o último elemento da lista menor


# 4. Faça a taboada feita em aula começando do número 9.

# In[ ]:


for a in range(9,0,-1):
  for b in range(10):
    print(a,' x ',b,' = ',a*b)


# <h1> Loop 3 <h1>

# Nessa aula vamos aplicar o que aprendemos até aqui com um pouco mais de profundiade e tem tipo de variável nova na área.
# *   **Dicionário:** váriavel com estrutura chave:valor, utilizado para armazenar valores e anexar eles em um índice de busca, esse índice (chave) não pode ser repetido enquanto os valores sim podem.
# 

# In[ ]:


#criando um dicionário e printando o valor da 
# Dicionário é um conjunto de chave e valor
dicionario = {'chave1':'valor1','chave2':'valor2','chave3':3}
dicionario['chave2']


# In[ ]:


#printando dicionário inteiro
dicionario


# In[ ]:


#printando items do dicionário
dicionario.items()


# In[ ]:


#printando valores do dicionário
dicionario.values()


# In[ ]:


#printando chaves do dicionario
dicionario.keys()


# In[ ]:


#percorrendo itens do dicionario com for
for a,b in dicionario.items():
  print(a,b)


# In[ ]:


#criando duas listas
lista_1=[1,2,3,4,5]
lista_2=[5,4,3,2,1]
#convertendo o zip das 2 listas em dict e atribuindo a um segundo dicionário
dicionario_2=dict(zip(lista_1,lista_2))
dicionario_2


# In[ ]:


#criando um terceiro dicionario
dicionario_3={}
#criando uma lista de cores e outra de adjetivos
cor = ['azul','verde','cinza']
adj = ['legal','top','top']
#percorrendo a lista e atribuindo ao dicionário chave e valor pelo zip das listas corres e adjetivos
for a,b in zip(cor, adj):
  dicionario_3[a]=b
dicionario_3


# In[ ]:


#criando um dicionario com dados reais e com alguns valores em listas
dicionario_full = {'usuario':'Peter','lingua':'pt-br','pet':['cachorro_1','cachorro_2']}
dicionario_full


# In[ ]:


#printando cada campo do dicionário em formato de json
print('nome do usuario: ', dicionario_full['usuario'])
print('lingua nativa: ',dicionario_full['lingua'])
#printando len da lista (quantidade de valores)
print('qtd de pet: ', len(dicionario_full['pet']))


# In[ ]:


#criando lista de 3 dicionários com estruturas iguais aos de cima
lista_dicionario_full =[{'usuario':'Peter','lingua':'pt-br','pet':['cachorro_1','cachorro_2']},
                        {'usuario':'Peter2','lingua':'pt-br','pet':['cachorro_1','cachorro_2']},
                        {'usuario':'Peter3','lingua':'es-ar','pet':'cachorro_2'}]
lista_dicionario_full


# In[ ]:


#printando dicionario e verificando se o type é diferente de string (lista) para printar o len desse paramêtro 
#caso não printando qtd = 1
for a in lista_dicionario_full:
  print('nome do usuario: ', a['usuario'])
  print('lingua nativa: ',a['lingua'])
  if type(a['pet'])!= str:
    print('qtd de pet: ',  len(a['pet']))
  else:
    print('qtd de pet: ',1)


# In[ ]:


#percorrendo valores do dicionário com for
for a in dicionario_full.values():
  print(a)


# In[ ]:


#percorrendo valores do dicionário e verificando se o type de algum deles é list, se for, 
#criando um novo for e percorrendo até range(len(a)) os valores
for a in dicionario_full.values():
  if type(a)==str:
    print(a)
  if type(a)==list:
    for b in range(len(a)):
      print(a[b])


# In[ ]:


#criando estrutura com varios dicionarios
varios_dict = {
  "aluno" : {
    "name" : "fulano",
    "year" : 1985
  },
  "aluno2" : {
    "name" : "ciclano",
    "year" : 1999
  },
  "aluno3" : {
    "name" : "Linus",
    "year" : 2021
  }
}
#criando for para percorrer os items do dicionario
for a,b in varios_dict.items():
  print(a,b)


# In[ ]:


#percorrendo os items do dicionario com enumerate
for a,b in enumerate(varios_dict.items()):
  print(a,b)


# In[ ]:


#percorrendo os items do dicionário com zip do enumerate
for a in zip(enumerate(varios_dict.items())):
  print(a)


# <h2> Dicas </h2>

# 
# 
# > O Dicionário é o mesmo formato do arquivo Json, é bastante usado para trabalhar com dados semi-estruturados.
# 

# In[ ]:


get_ipython().system('wget https://raw.githubusercontent.com/LearnWebCode/json-example/master/animals-1.json')


# In[ ]:


import json
with open('animals-1.json') as json_file:
    itemData = json.load(json_file)
itemData


# <h1>Exercícios:<h1>

# 1. Percorra cada pet no dicionário acima e imprima sua espécie.

# In[ ]:


# Primeiro itemData é uma lista e não um dicionário. Pode ver que tem '[]'no começo no fim dele
#Logo a ideia é trabalhar com uma lista de dicionários 
for a in itemData:
  print(a['species'])


# 2. Percorra cada pet no dicionário e imprima e pet com maior quantidade de dislikes.

# In[ ]:


maior, nomes = [], []
for b in itemData:
  maior.append(len(b['foods']['dislikes']))
  nomes.append(b['name'])
print('O pet com maior número de dislikes é o', nomes [maior.index(max(maior))])


# In[ ]:


#Ou
pet =''
len1=0
for a in itemData:
  print(len(a['foods']['dislikes']), a['name'])
  if len1 < len(a['foods']['dislikes']):
    len1 = len(a['foods']['dislikes'])
    pet=a['name']
  pet


# 
# 3. Conte o total de comidas citadas no dicionário e quantas se repetem.
# 

# In[ ]:


#Criar uma lista vazia e atribuir todos os valores
comidas=[]
for a in itemData:
  for b in a['foods']['dislikes']:
    comidas.append(b)
  for c in a['foods']['likes']:
      comidas.append(c)
comidas 


# In[ ]:


lista.count('valor')#conta a ocorrência do valor na lista
for a in comidas:
  print(comidas.count(a),a) 


# # Funções Nativas

# 
# 
# 
# <h1> Funções Nativas Python </h1>
# 
# <b> Geral:</b><br>
# O python possui diversas funções prontas e já instaladas nativamente para uso, abaixo tem uma lista dessas funções
# <br> <br>
# 
# ![LxITc.png](data:image/png;base64,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)
# 
# 
# 
# 

#  Você também pode consultar essas funções utilizando o comando abaixo:<br> 
# 
# 
# 
# 

# In[ ]:


dir(__builtins__)


# **sorted()**

# In[ ]:


lista = [1,2,3,4,3]
sorted(lista)


# **max()**

# In[ ]:


max(lista)


# **min()**

# In[ ]:


min(lista)


# **len()**

# In[ ]:


len(lista)


# **str()**

# In[ ]:


str(lista)


# **set()**

# In[ ]:


set(lista)


# **help(estrutura)**

# In[ ]:


help(lista)


# **eval(conta aritmética em string)**

# In[ ]:


eval('10+1-7')


# **id()**

# In[ ]:


#endereço da lista
id(lista)


# In[ ]:


#endereço da lista após adicionar mais um elemento
id(lista.append(10))


# In[ ]:


#copiando a lista com copy
lista_2 = lista.copy()


# In[ ]:


#verificando endereço da lista original
id(lista)


# In[ ]:


#verificando endereço diferente da cópia da lista
id(lista_2)


# **input()**

# In[ ]:


input()


# **sum()**

# In[ ]:


sum(lista)


# <h2> Dicas </h2>

# 
# 
# > Nas [documentações do Python](https://docs.python.org/3/library/functions.html) tem uma lista com cada uma das funções citadas aqui e as outras não mencionadas, essa lista é sempre atualizada.
# 

# <h1>Exercícios:<h1>

# Utilize pelo menos outras 3 funções contidas no link acima.

# In[ ]:


tuple([1,2,3,4,5])


# In[ ]:


chr(10234)


# In[ ]:


list(reversed(tuple([1,2,3,4,5])))


# # Funções

# <h1>criação da primeira função</h1>
# def primeira_func():
#   return "primeira função"
# primeira_func()

# In[ ]:


#pode dar o nome que quiser desde que não seja numeros nem palavras reservadas do python
def seg_func (x,y):
  return x+y
seg_func(10,7)


# In[ ]:


#pode usar funções built-in dentro da função
def contador_lista(lista):
  return len(lista),sum(lista)
contador_lista([0,1,2,3,4,5,6,7,8,9])


# In[ ]:


#função verifica se é par, atribui numa variável e retorna resposta "o numero é"+variavel
def  verifica_par(x):
  if x % 2==0:
    result = 'par'
  else:
    result='impar'
  return 'o numero é '+result
verifica_par(11)


# In[ ]:


#lista com numeros de 1 a 9
lista=[1,2,3,4,5,6,7,8,9]
#utilizando o map para aplicar a função verifica_par na lista e atribuindo o resultado em x
x = map(verifica_par, lista)
#printando a list de x porque o map retorna um construtor
print(list(x))


# In[ ]:


#criando nova função verifica_par e atribuindo True ou False na variavel que vai retornar
def  verifica_par_filtro(x):
  if x % 2==0:
    result = True
  else:
    result= False
  return result


# In[ ]:


#utilizando o filter para aplicar a nova função verifica_par em uma lista e atribuindo a x
x = filter(verifica_par_filtro, [1,2,3,4,5,6,7,8,9])
#printando list de x porque o filter retorna um construtor
print(list(x))


# In[ ]:


#criando função taboada que recebe um número e percorre o for com print da multiplicação desse numero até o range definido
def taboada (x):
  for a in range(11):
    print (x,' x ',a,' = ',x*a)


# In[ ]:


taboada(9)


# In[ ]:


#criando variavel que recebe x e y e atribuindo x e y default
def padrao (x=10,y=5):
  return x+y


# In[ ]:


#print da função padrão acima sem passar parâmetros
print(padrao())
#print da função padrão acima passando o valor de x
print(padrao(x=15))
#print da função padrão acima passando o valor de x e de y
print(padrao(x=15,y=30))
#print da função padrão acima passado 2 valores
print(padrao(33,37))
#print da função padrão acima passando o valor de y
print(padrao(y=29))


# In[ ]:


#criando função sem print e sem return
def npadrao (x=10,y=10):
  x+y


# In[ ]:


#printando a função
print(npadrao())


# In[ ]:


#criando função cadastro com input de nome e sobrenome e retornando nome e sobrenome do input
def cadastro():
  print("digite seu nome:")
  nome=input()
  print("digite seu sobrenome:")
  snome=input()
  return nome,snome


# In[ ]:


#criando variavel usuario e chamando funcao cadastro
user = cadastro()
#printando variavel usuario
print(user)


# <h1>Exercícios:<h1>

# 1. Crie uma função que receba o input do cpf e nome do usuário.
# 
# 

# In[ ]:


def cadastro ():
  print('digite seu nome')
  nome=input()
  print('digite seu cpf')
  cpf=input()
  print(nome, cpf)
cadastro()


# 2. Agora nessa mesma função coloque o retorno como um dicionário onde a chave é o cpf e o valor o nome do usuário.

# In[ ]:


def cadastro ():
  print('digite seu nome')
  nome=input()
  print('digite seu cpf')
  cpf=input()
  dicio = dict({cpf:nome})
  print(dicio)
  return dicio
user=cadastro()
print(user)


# 3. Crie uma função para retornar a quantidade de CPF cadastrados

# In[ ]:


def cadastro ():
  cpfs=[]
  continuar=''
  while continuar !='não':
      print('digite seu nome')
      nome=input()
      print('digite seu CPF')
      cpf=input()
      cpfs12.append(cpf)
      print('quer continuar?')
      continuar = input()
  return len (cpfs)
qtd =ncadastro()
qtd


# <h2> Funções Lambda  </h2>

# Funções Lambdas são funções no python que nos permite construir em apenas uma linha de código funções como vimos anteriormente.

# In[ ]:


#criando função lambda que soma x com x e atribuindo a f1
f1 = lambda x:x+2
#criando função lambda que eleva x ao quadrado e atribuindo a f2
f1(10)
#printando f1 e passando o x
f2 = lambda x,y:x+y
#printando f2 e passando o x
f2(10,12)


# In[ ]:


#criando funcao de verificar par com lambda
ver_par = lambda x: 'par' if x %2==0 else 'impar'
#chamando função verifica par
ver_par(11)


# In[ ]:


#utilizando o map para executar a função verifica par em uma lista e atribuindo a variavel par
#convertendo o map para lista
#criando funcao de verificar par com lambda
ver_par_filter = lambda x: True if x %2==0 else False
#chamando função verifica par
ver_par_filter(11)
#printando variavel par
lista=[1,2,3,4,5,3,6,4,3]
pares = list(filter(lambda x: True if x %2==0 else False,lista))
print(pares)


# In[ ]:


#criando função lambda verifica par dentro do map e passando uma lista e convertendo resultado para lista

#printando o resultado de par
#list(map(lambda x: 'par' if x %2==0 else 'impar' ,lista))
list(filter(ver_par_filter,lista))


# In[ ]:


#criando função lambda dentro do filter e passando como lista range(10)
#convertendo os valores para lista e atribuindo a variavel par
list(filter(ver_par_filter,range(10)))
#printando a variavel par


# In[ ]:


#importando o modulo reduce da biblioteca functools
#biblioteca é um diretório de modulos 
from functools import reduce

#atribuindo o resultado do reduce a uma nova variável e criando uma função lambda para somar x e y e passando lista range(10)
# irá acumular as soma dos números de 0 a 9 na variável x
#printando o resultado acima
reduce(lambda x,y:x+y, range(11))

# equivalente a criar x = 0, percorrer um for range(10) e somar x com y percorrido no for
y=0
for a in range(11):
  y+=a
print(y)


# In[ ]:


#recriando o reduce acima porém com x iniciando em 100
 # irá acumular as soma dos números de 0 a 9 na variável x, 
                                          # porém, a variável x é inicializada como 100

print(reduce(lambda x,y:x+y, range(100)))

# equivalente a criar x = 0, percorrer um for range(10) e somar x com y percorrido no for
y=0
for a in range(100):
  y+=a
print(y)
# equivalent to


# In[ ]:


#criando uma função lambda que retorna a soma de 3 valores recebidos
soma = lambda a,b,c : a+b+c
soma(10,20,30)


# <h2> Dicas </h2>

# 
# 
# > A gama de conhecimentos que vimos até aqui já resolve a grande maioria dos problemas que aparecem no dia a dia. Claro que ainda há muito pela frente, mas essa base será utilizada durante o curso todo e a hora de praticar é o momento que mais absorvemos o conteúdo.
# 

# <h1>Exercícios:<h1>

# 1. Crie uma função Lambda para retornar a soma de 4 valores.
# 

# In[ ]:


f1 = lambda a,b,c,d: a+b+c+d
f1(1,2,3,4)


# 2. Utilize uma função filter para retornar somente os números pares da lista abaixo.<br>
# [5,2,5,7,4,2,6,10,342,54,23,6,7,9,12]
# 

# In[ ]:


par = list(filter(lambda x: x%2==0,[5,2,5,7,4,2,6,10,342,54,23,6,7,9,12]))
#retona os números printando a variável par
print(par)


# 3. Utilize a função reduce e retorne a soma da lista anterior.

# In[ ]:


from functools import reduce
#atribuindo o resultado a uma nova variável e criando uma função lambda para somar
r = reduce(lambda x,y:x+y, [5,2,5,7,4,2,6,10,342,54,23,6,7,9,12])
#irá acumular as soma dos valores printando o resultado acima
print(r)


# # Classes

# 
# <h1> Classes Python </h1>
# 
# <b> Geral:</b><br>
# Classes são usadas como prótotipos para instanciar objetos, a programação orientada a objetos é um assunto que demandaria um curso inteiro com esse tema para conseguir passar por toda sua abrangência. Como python é uma programação orientada a objetos desde de sua fundação, não podemos deixar de ver os principais conceitos e termos aqui. Fornecemos na plataforma bibliografia para quem quiser se aprofundar mais.
# <br> <br>
# 
# 
# 
# 
# 

# <b>Objetos</b> <br>
# Objetos são compostos basicamente de dois atributos: 
# 
# 1.   Estado -> Informações salvas nos atributos dos objetos.
# 2.   Comportamento -> ações que o objeto pode tomar, representam as funções e métodos dentro do objeto.
# <br><br>
# **Classe**
# <br>
# Classes são usadas para instanciar objetos, para ficar menos abstratos vamos aplicar em um exemplo ilustrativo. 
# 
# 
# > Criamos a **Classe Carro** <br> 
# **Objetos** dessa classe poderiam ser **Fiat Uno**, **VW Gol**, **Corolla**
# <br>
# **Estado (Atributos)** seriam **Gasolina**, **óleo**, **água**...etc. <br>
# **Comportamentos (Funções e métodos)** seriam **acelerar**, **freiar**... etc.
# 
# 
# 

# Vamos ver como isso funcionaria na prática:

# In[ ]:


class Carro():
  def __init__(self, litros, velocidade=0):
      self.litros = litros
      self.velocidade = velocidade

  def gasolina(self,litros=20):
    print("Tem ",self.litros," de gasolina")

  def acelera(self,velocidade=0):
    velocidade=self.velocidade
    if self.velocidade < 120:
      self.litros = self.litros-2
      print("Velocidade: ",self.velocidade,"\nQuantidade de litros de gasolina: ",self.litros)
    else:
      self.litros = self.litros-5
      print("Velocidade: ",self.velocidade,"\nQuantidade de litros de gasolina: ",self.litros)


# In[ ]:


#pode dar o nome que quiser desde que não seja numeros nem palavras reservadas do python
uno = Carro(litros=10) 

uno.gasolina()#acessando função gasolina
uno.velocidade=120
uno.acelera()
uno.velocidade=99
uno.acelera()
uno.litros=uno.litros+32
uno.acelera()


# <b> Herança </b>
# <br> As classes podem herdar comportamentos e estados de outra classe, seguindo o exemplo acima, poderiamos ter a Classe Automóvel e a classe carro herdar os estados e comportamentos acima, se tornando uma sub classe de Automóveis.

# In[ ]:


class fiat_uno(Carro):
  def __init__(self):  # o construtor da subclasse chama o construtor da superclasse
                         # com parametros desejados
    Carro.__init__(self,litros=9,velocidade = 50)
    
  def escada(self):
    print("Nova velocidade ",self.velocidade*10," KM/h")
 


# In[ ]:


tunado = fiat_uno()
tunado.acelera()
tunado.escada()


# In[ ]:


tunado.litros=17
tunado.acelera()


# In[ ]:


uno.escada()


# **Sobrecarga de operador** (Operator Overloading)
# Classes podem interceptar operadores especiais e sobrescrevê-los. Esses métodos são definidos por um duplo underscore antes e depois da escrita. Exemplos de operadores especiais são:
# 
# - <font color='blue'>\_\_init\_\_</font> construtor do objeto
# - <font color='blue'>\_\_repr\_\_</font> método que gera uma representação da classe
# - <font color='blue'>\_\_add\_\_</font> método que define a operação de soma <font color='blue'>+</font>
# - <font color='blue'>\_\_lt\_\_</font>, <font color='blue'>\_\_gt\_\_</font>, para comparações X < Y, X > Y
# - e outras...

# In[ ]:


class pessoa():
    def __init__(self,nome = '', sobrenome = '', idade = 0):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade
        
    def __lt__(self,p):  # operador '<'
        return(self.idade < p.idade)  # retorna True se a idade da instancia da classe for menor
    
    def __gt__(self,p):  # operador '>'
        return(self.idade > p.idade)


# In[ ]:


p1 = pessoa(nome='Peter',sobrenome='Almeida',idade=50)    # instancia um objeto 'pessoa'
p2 = pessoa(nome='Daniel',sobrenome='Soria',idade=52) # instancia outro objeto 'pessoa'

if p1 < p2:
    print(p1.nome, ' eh mais novo que ',p2.nome)
else:
    print(p1.nome, ' nao eh mais novo que ',p2.nome)
    


# <br>**Indo além com classes**
# 
# 1.   [Inglês](https://www.tutorialspoint.com/python/python_classes_objects.htm) -> Tutorial com teoria e prática com mais exemplos.
# 2.   [Português](https://panda.ime.usp.br/pensepy/static/pensepy/13-Classes/classesintro.html) -> Tutorial com teoria, ilustrações e prática com mais exemplos.
# 
# 

# <h2> Dicas </h2>

# 
# 
# > Você pode utilizar as classes para organizar as funções e dados juntos, na [documentação](https://docs.python.org/pt-br/3/tutorial/classes.html) você encontra uma descrição completa de como utilizar e como não utilizar. <br><br> Lembre-se que por em prática é uma etapa fundamental para o aprendizado, então sempre tente fazer todos os exercícios.
# 

# <h1>Exercícios:<h1>

# 1. Recrie a classe Carro e adicione um novo atributo e um novo método (função).
# 
# 

# In[ ]:


class Carro():
  def __init__(self, litros, velocidade=0, buzina='BIBI!'):
    self.litros = litros
    self.velocidade = velocidade
    self.buzina= buzina

  def aciona_buzina(self, litros=20):
    print(self.buzina)

  def acela (self, velocidade=0):
    velocidade=self.velocidade
    if self.velocidade <120:
      self.litros = self.litros-2
      print ("velocidade:", self.velocidade,"\nQuantidade de litros de gasolina: ", self.litros)
    else:
      self.litros = self.litros-5
      print("velocidade:", self.velocidade,'\nQuantidade de litros de gasolina:', self.litros)


# 2. Crie uma sub classe a partir da classe criada no exercício 1.

# In[ ]:





# 3. Sobreescreva um dos operadores dentro de uma nova classe.

# In[ ]:





# 4. Crie uma classe chamada Calculadora com os atributos Digito 1 e Digito2, crie os métodos de adição e de subtração.

# In[ ]:





# 5. Crie uma subclasse de Calculadora e adicione os métodos de divisão, multiplicação e exponencial.

# In[ ]:





# # Operações com Listas 

# 
# ![images.png](data:image/png;base64,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)</b> <br>Consultor: Peterson Almeida <br>
# 
# 
# 
# <h1> Operações com Lista </h1>
# 
# <b> Geral:</b><br>
# Vimos já um poucos de listas, agora vamos entrar mais afundo nas operações que podemos fazer em objetos do tipo lista.
# <br> <br>
# 
# 
# 
# 
# 

# <b>Operações com Listas</b> <br>
# Abaixo tem as operações que temos prontas para utilizar com listas: 
# 
# 1.   Append() -> Adiciona um elemento no final da lista.
# 2. Clear() -> Remove todos os itens da lista.
# 3.   Copy() -> Faz uma cópia da lista.
# 4. Count() -> Retorna a quantidade de elementos da lista.
# 5. Extend() -> Adiciona elementos iteráveis no final da lista.
# 6. Index() -> Retorna o endereço do elemento da lista.
# 7. Insert() -> Insere um elemento na lista com o endereço específicado.
# 8. Pop() -> Remove um elemento do endereço especifícado.
# 9. Remove() -> Remove o primeiro elemento encontrado pelo valor específicado.
# 10. Reverse() -> Inverte a ordem da lista.
# 11. Sort() -> Ordena a lista por algum chave específicada.
# 

# **Append()**

# In[ ]:


lista_1 =[1,2,4,3,5,8,7,9]
print(lista_1)
lista_1.append(20)
print(lista_1)
lista_1.append([20,10])
print(lista_1)
lista_1.append([20])
print(lista_1)
lista_1.append(5)
print(lista_1)


# **Copy()**

# In[ ]:


lista_2 = lista_1.copy()
print(lista_1)
print(lista_2)
lista_2.append(9)
print(lista_1)
print(lista_2)
lista_3 = lista_2
print(lista_2)
print(lista_3)
lista_3.append(333)
print(lista_1)
print(lista_2)
print(lista_3)
print(id(lista_1))
print(id(lista_2))
print(id(lista_3))


# **Clear()**

# In[ ]:


lista_del = [10,3,2,4,[2,4],7]
print(lista_del)
lista_del.clear()
print(lista_del)


# **Count()**

# In[ ]:


print(lista_1.count(2))
print(lista_2.count(9))
print(lista_2.count(20))
print(lista_2.count([20]))


# **Extend()**

# In[ ]:


print(lista_1)
lista_1.extend([10,30,20,30])
print(lista_1)
lista_1.extend(lista_1)
print(lista_1)
lista_4 = [10,9,8,7,5,6,4,2,3,1,2,3]
lista_4.extend((3,3,3))
print(lista_4)


# **Index()**

# In[ ]:


print(lista_1.index(9))
print(lista_1.index(9,10))
print(lista_1.index(9,2,40))
print(lista_1.index(9,10,20))


# **Insert()**

# In[ ]:


print(lista_4)
lista_4.insert(2,77)
print(lista_4)


# **Pop()**

# In[ ]:


print(lista_4)
lista_4.pop(2)
print(lista_4)
lista_4.pop(-1)
print(lista_4)


# **Remove()**

# In[ ]:


print(lista_4)
lista_4.remove(2)
print(lista_4)
lista_4.remove(-1)
print(lista_4)


# **Reverse()**

# In[ ]:


print(lista_4)
lista_4.reverse()
print(lista_4)
lista_4.reverse()
print(lista_4)


# **Sort()**
# 
# 

# In[ ]:


print(lista_4)
lista_4.sort()
print(lista_4)
lista_4.reverse()
print(lista_4)
print(sorted(lista_4))
print(lista_4)
lista_4.sort(reverse=True)
print(lista_4)
print(5*"--")
lista_5=['Peter','Fulano','Ciclano','Pet']
print(lista_5)
lista_5.sort(key=len)
print(lista_5)
lista_5.sort(key=len,reverse=True)
print(lista_5)


# <h2> List Comprehension </h2> <br> List Comprehension é um dos grandes marcos de Python, podemos criar loop dentro de uma lista para gerar ela.

# In[ ]:


lista_6 =[a for a in range(10)]
print(lista_6)


# In[ ]:


lista_7 = [a for a in range(10) if a%2==0]
print(lista_7)


# <h1>Exercícios:<h1>

# 1. Construa uma lista de inteiros e ordene elas do maior para o menor.
# 
# 

# In[ ]:





# 2. Adicione os valores 10,7,33,22 com uma única linha de código e deixe-os ordenados também em uma segunda linha de código.

# In[ ]:





# 3. Gere uma lista de nomes e ordene ela pelo tamanho de cada nome.

# In[ ]:





# 4. Crie uma lista que vá de 1 até 100.

# In[ ]:





# 5. Em uma nova lista adicione somente os valores ímpares de 1 a 100.

# In[ ]:





# <h1>Strings</h1> <br> 
# Strings é uma das estruturas com mais métodos disponíveis, devido a sua abrangência e complexidade.<br> Vamos ver aqui uma lista com os principais métodos e ver exemplos de alguns deles.<br><br>
# 
# 1.   capitalize()	-> Converte a primeira letra para maiúsculo.
# 2. casefold()	-> Converte a string para minúsculo.
# 3. center()	-> Retorna a string como centro e preenche com espaços o restante do tamanho.
# 4. count()	-> Retorna o tamanho da palavra.
# 5. encode()	-> Retorna a string codificada.
# 6. endswith()	-> Retorna um booleano se o final da string corresponder ao valor específicado.
# 7. find()	->Procura um determinado valor e retorna a posição dele caso encontrado.
# 8. isdecimal()	-> Retorna um booleano dizendo se todos os caracteres são decimais.
# 9. isdigit()	-> Retorna um booleano dizendo se todos os caracteres são dígitos.
# 10. islower()	-> Retorna um booleano caso todos os caracteres sejam minúsculos
# 11. isnumeric()	-> Retorna um booleano caso todos os caracteres sejam numéricos.
# 12. isupper()	-> Retorna um booleano caso todos os caracteres sejam maiúsculos.
# 13. join()	-> Junta dois elementos de um iterável em uma string.
# 14. lower()	-> Converte a string para minúsculo.
# 15. replace()	-> Altera determinado valor de uma string por outro.
# 16. split()	-> Divide a string por algum determinado separador.
# 17. splitlines()	-> Separa a string por linhas.
# 18. startswith()	-> Retorna um booleano se a string começar com determinado valor.
# 19. strip()	-> Retorna a string recortada por determinado valor.
# 20. upper()	-> Converte a string em letras maiúsculas
# 
# 
# <br> Esses são os 20 métodos mais utilizados, entretando existe mais de 40 métodos que podem ser consultados na documentação do python ou nesse [link](https://www.w3schools.com/python/python_ref_string.asp) com tutoriais. <br>
# 
# 

# In[ ]:


texto = 'vou Treinar todo Dia Python'
print(texto.capitalize())
print(texto)


# In[ ]:


print(texto)
print(texto.casefold())
print(texto.upper())
print(texto.lower())


# In[ ]:


texto.find('Python')


# In[ ]:


texto.split()


# In[ ]:


texto.strip('vou')


# In[ ]:


texto.split('t')


# In[ ]:


texto.split('t')[0]


# In[ ]:


texto.split()[-1]


# In[ ]:


texto.strip('Python')


# In[ ]:


texto.replace('vou','Vamos')


# In[ ]:


type(texto.split())


# In[ ]:


texto_2 = 'vou treinar todos os dias Python \npelo menos 2 horas e 30 minutos por dia'
print(texto_2)


# In[ ]:


texto_2.splitlines()


# In[ ]:


texto_2.isalnum()


# In[ ]:


texto_2.isnumeric()


# In[ ]:


numeros = [a for a in texto_2.split() if a.isnumeric()==True]
numeros


# In[ ]:


nomes = [a for a in texto_2.split() if a[0].isupper()==True]
nomes


# In[ ]:


nomes2 = [a for a in texto_2.split() if a.istitle()==True]
nomes2


# In[ ]:


texto_2.center(100)


# In[ ]:


lista_5


# In[ ]:


text_3 = " ".join(lista_5)
text_3


# <h1>Exercícios:<h1>

# 1. Crie uma paragráfo contando uma experiência de vida e armazene isso em uma string. Depois retorne a quantidade de palavras desse parágrafo.

# In[ ]:





# 2. Conte a quantidade de nomes próprios e de números que aparecem na história.

# In[ ]:





# 3. Conte a quantidade de vogais que aparecem na história.

# In[ ]:





# 4. Conte a quantidade de linhas que aparece na string.

# In[ ]:





# 5. Utilize pelo menos mais 3 métodos próprios pra string que não apareceu em aula mas estão na referência.

# In[ ]:





# # Operações com Tuplas e Dicionários

# 
# 
# <h1> Operações com Tuplas e Dicionários </h1>
# 
# <b> Geral:</b><br>
# Vimos já um poucos de tuplas e dicionários, agora vamos entrar mais afundo nas operações que podemos fazer em objetos desse tipo.
# <br> <br>
# 
# 
# 
# 
# 

# <b>Operações com Tuplas</b> <br>
# Diferente de listas e strings, a quantidade de métodos para Tuplas são bem limitados, sendo eles: 
# 
# 1.   Count() -> Conta a quantidade de ocorrência de determinado valor.
# 2. Index() -> Procura na tupla determinado valor e retorna seu endereço.
# 

# **Count()**

# In[ ]:


tupla_1 = (1,2,4,7,5,6,(4,3),1,2,1)
print(tupla_1)
print(tupla_1.count(1))
print(tupla_1.count(3))
tupla_2 = ("oi","tchau","boa tarde")
print(tupla_2)
print(tupla_2.count("oi"))
print(tupla_2.count("o"))


# **Index()**

# In[ ]:


print(tupla_1)
print(tupla_1.index((4,3)))
print(tupla_2)
print(tupla_2.index("boa tarde"))
print(tupla_2.index("o"))


# **Usando funções do python para tuplas** <br> Por mais que temos um leque de opções limitados para métodos próprios para tuplas, podemos utilizar métodos gerais do python que são compatíveis com operações com tupla, ou então construir nossos próprios métodos.

# In[ ]:


tupla_3 = tupla_1 + tupla_2
print(tupla_3)
del tupla_3
print(tupla_3)


# In[ ]:


tupla_3 = (10,203,40,7)*2
print(tupla_3)
print(id(tupla_3))
lista = list(tupla_3)
lista.sort()
tupla_3= tuple(lista)
print(id(tupla_3))
tupla_3


# In[ ]:


(valor_1,valor_2,valor_3)=tupla_2
print(valor_1)
print(valor_2)
print(valor_3)


# <h2> Bônus: Set </h2> <br> <b>Set</b> é uma estrutura que não vimos ainda, mas é para muitos cenários bem útil, esse objeto tem sintaxe de dicionário, mas não permite valores duplicados, são imutáveis e não possuem enereço para os valores dentro dele.<br><br>
# Os métodos que ele possui são os seguintes:
# <br>
# 1. add() ->	Adiciona um elemento.<br>
# 2. clear()	-> Remove todos os elementos.<br>
# 3. copy()	->	Retorna uma cópia.<br>
# 4. difference()	->	Retorna a diferença entre 2 ou mais sets.<br>
# 5. difference_update()	->	Remove os itens desse set que já está contido em algum outro.<br>
# 6. discard()	->	Remove algum item específico.<br>
# 7. intersection()	->	Retorna um set que é a intersecção entre outros dois sets.<br>
# 8. intersection_update()	->	Remove os items desse set que não estão especificados em outro set.<br>
# 9. isdisjoint()	->	Retorna se os sets tem uma intersecção ou não.<br>
# 10. issubset()	->	Retorna se outro set contém esse set ou não.<br>
# 11. issuperset()	->	Retorna se esse set contém outro set ou não<br>
# 12. pop()	->	Remove um elemento desse set.<br>
# 13. remove()	->	Remove um elemento especificado.<br>
# 14. symmetric_difference()	->	Retorna um set com a diferença simétrica entre os dois sets.<br>
# 15. symmetric_difference_update()	->	insere as diferenças simétricas entre esse set e outro.<br>
# 16. union()	->	Retorna um set contendo a união dos sets.<br>
# 17. update()	->	Atualiza o set com a união dele com outro set.<br> <br> Como alguns tem funcionamento similares aos que vimos em outros construtores, vamos focar com os novos específicos para set.

# **Diference()**

# In[ ]:


set_1 = {1,2,3,4,5,6,7}
set_2 = {0,3,4,5,6,7,8,9}
print(set_1.difference(set_2))
print(set_2.difference(set_1))


# **Diference_update()**

# In[ ]:


print(set_1)
set_1.difference_update(set_2)
print(set_1)


# **intersection()**

# In[ ]:


print(set_2)
set_3={1,2,3,4,7,0,9}
print(set_3)
print(set_2.intersection(set_3))


# **intersection_update()**

# In[ ]:


print(set_2)
print(set_3)
set_2.intersection_update(set_3)
print(set_2)


# **isdisjoint()**

# In[ ]:


print(set_1)
print(set_2)
print(set_3)
set_4={77,33}
print(set_4)
print(set_2.isdisjoint(set_3))
print(set_3.isdisjoint(set_1))
print(set_3.isdisjoint(set_4))


# **issubset()**

# In[ ]:


set_5={1,2,3,4,5}
set_6={0,1,2,3,4,5}
print(set_5)
print(set_6)
print(set_5.issubset(set_6))
print(set_6.issubset(set_5))


# **symmetric_difference()**

# In[ ]:


print(set_5)
print(set_3)
print(set_5.symmetric_difference(set_3))


# **Union**

# In[ ]:


print(set_5)
print(set_3)
print(set_5.union(set_3))


# **Update()**

# In[ ]:


print(set_5)
print(set_3)
set_5.update(set_3)
print(set_5)


# **Complementando**

# In[ ]:


set_1 = {1,2,3,4,5}
print(set_1)
tupla=(1,2,3,4,5,6,5,4,6,7)
print(tupla)
print(set(tupla))
set_2={1,1,2,2,3,3,4,5,6,7,8,9,0}
print(set_2)


# In[ ]:


set_3 ={True,False,True,False,0,2,3,"oi"}
print(set_3)#reparem que ele rmeoveu o 0


# <h1>Exercícios:<h1>

# 1. Crie uma tupla e ordene ela.
# 
# 

# In[ ]:





# 2. Remova todos os valores duplicados da tupla.

# In[ ]:





# 3. Crie uma função que busque um determinado valor em uma tupla e retorne a quantidade de vezes que esse valor aparece.
# 

# In[ ]:





# 4. Crie dois sets e atribua no primeiro a diferença simétrica entre os dois.

# In[ ]:





# 5. Faça a união entre os dois sets e salve o resultado em um terceiro set.

# In[ ]:





# <h1>Dicionários</h1> <br> 
# Dicionários como já vimos, armazena valores em pares de chave:valor. É muito utilizado com dados semi-estruturados e para trabalhar com arquivos JSON<br><br>
# 
# 1.   clear()	-> Limpa todos os elementos do dicionário.
# 2. copy()	-> Retorna uma cópia do dicionário.
# 3. fromkeys(x,y)	-> Retorna um dicionário com as chaves e opcionalmente pode já atribuir os valores.
# 4. get()	-> Retorna o valor da chave especificada.
# 5. items()	-> Retorna uma tupla contendo a chave e valor de cada elemento.
# 6. keys()	-> Retorna todas as chaves existentes no dicionário.
# 7. pop()	-> Remove o elemento com a chave especificada.
# 8. popitem()	-> Remove o último elemento com chave:valor.
# 9. setdefault()	-> Retorna o valor da chave específicada. Caso não exista, insere a chave com o específicado valor.
# 10. update()	-> Atualiza o dicionário com a chave:valor especificados.
# 11. values()	-> Retorna todos os valores dentro do dicionário.
# 
# 
# <br> Vamos seguir a mesma estratégia que usamos com set e focar nos novos métodos que apareceram. <br>
# 
# 

# **Fromkeys()**

# In[ ]:


chaves=["id_1","id_2","id_3"]
dicionario_1 = dict.fromkeys(chaves)
print(dicionario_1)

chaves=["id_1","id_2","id_3"]
valor=7
dicionario_2 = dict.fromkeys(chaves,valor)
print(dicionario_2)

chaves=["id_1","id_2","id_3"]
valores=[12,123,1234]
dicionario_3 = dict.fromkeys(chaves,valores)
print(dicionario_3)


# **Get()**

# In[ ]:


print(dicionario_3.get("id_1"))
print(dicionario_3.get("id_4","Não tem"))


# **Items()**

# In[ ]:


dicionario_3.items()


# **Keys()**

# In[ ]:


dicionario_3.keys()


# **Setdefault()**

# In[ ]:


print(dicionario_3.setdefault("id_3",333))
print(dicionario_3.setdefault("id_4",333))


# **Values()**

# In[ ]:


print(dicionario_3.values())
print(type(dicionario_3.values()))
print(dicionario_3['id_3'])
print(type(dicionario_3['id_3']))
print(dicionario_3['id_3'][0])
print(dicionario_3['id_4'])


# <h1>Exercícios:<h1>

# 1. Crie um dicionário com nome, sobrenome e apelido de 3 usuários.

# In[ ]:





# 2. Procure o atributo idade para o usuário 1 e caso não tenha adicione o valor 30 nesse campo.

# In[ ]:





# 3. Conte a quantidade de nomes e sobrenomes contidos no dicionário.

# In[ ]:





# 4. Verifique se há dois nomes repetidos.

# In[ ]:





# # Principais Dúvidas

# <h1> Principais duvidas de Python </h1>
# 
# <b> Geral:</b><br>
# Uma das principais competências para programar é resolvr rros de códigos, ou podemos chamar pelo famoso termo Debugar o código. Vamos explorar os [principais erros](https://stackoverflow.com/questions/tagged/python?sort=MostFrequent&edited=true) cometidos na linguagem e como solucioná-los.
# <br> <br>
# 
# 
# 
# 
# 

# <b>Como solucionar um erro</b> <br>
# A lista abaixo tem as principais formas de verificar o motivo do erro do código, principalmente no começo, o Stackoverflow vai resolver uma grande parte delas. 
# 
# 1.   **StackOverflow** é sempre o primeiro acesso quando um mensagem de erro aparace, fazer as buscas em inglês aumenta muito a probabilidade de encontrar uma resposta.
# 2. **Github:** como a maior parte dos módulos Python estão no github e além disso existe muitos projetos lá que utilizam esses módulos, existe uma grande probabilidade de já terem reportado esse erro lá em algum discussão.
# 3. **Documentação:** A documentação serve para uma análise mais detalhista do porquê do erro do código, caso você esteja usando uma versão nova ou antiga você pode encontrar o motivo do não funcionamento dentro de alguma release.
# 4. **Consulta:** 1% das vezes que você procurar corretamente e não encontrar a resposta em nenhum desses lugares, é a hora de você criar um tópico no repositório, stackoverflow ou consultar alguém mais experiente na linguagem.
# 

# **Lendo os erros** <br>
# Antes de sair por ai caçando o motivo do erro, é de extrema importância que você aprenda a ler o erro, muitas vezes ele já explicitando o que você deve fazer para corrigir. 

# **Erro de sintaxe**

# In[ ]:


if 30 >20 #:
  print("maior")


# In[ ]:


lista  [1,2,3,4] #as vezes o erro da sintaxe faz o compilador entender outra coisa, como uma não criação de variável
(lista)


# **Divisão por zero**

# In[ ]:


10/0


# **Erros de tipos diferentes não compatíveis em operações**

# In[ ]:


"2"+'2'


# **Uso de função de uma biblioteca não importada ainda**

# In[ ]:


from functools import reduce
reduce(lambda x,y:x+y, range(10))


# **Alterar lista original**

# In[ ]:


original=[1,2,3,4,5]
copia = original.copy()
copia.append(7)
print(original, copia)


# <h1>Exercícios:<h1>

# 
# 
# 1. Conserte cada erro visto e adicione comentários explicando o que fez.
# 
# 

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# # Outros
# 

# In[ ]:


def fib(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)

