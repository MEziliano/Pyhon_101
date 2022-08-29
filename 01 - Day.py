#################################################################
#  01 - Varaibles, Data Types and operators
#################################################################
# Variables (variáveis )
# Armazenar valores (dados) e _reusar)
### Nota: é importante ter inglês técnico
x = 10
a = 5
b = 20
cor = "vermelho"

a = 10
b = 20 
a = 5
a+b  # Sequence matter... So: the resul will be 25 and not 30
#----------------------------------
# Como criar variáveis na prática?
#----------------------------------
a = 10
b = 20
c = 30
print("Hello World")

# ainda sobre função print
# Sem variável
print(10+20)
print(10-20)
print(10/20)
print(10*20)
# Com variável 
print(a+b)
print(a-b)
print(a*b)
print(a/b)

#  02 - Data Types (tipos de dados)

# numbers = 3, 100 , -20, 10.20, 50
# Strings = "Murilo", '3', "Python", 'maratona'
# Boolean  = True, False (On/Off)
string = "That's my life" # but what if...
string = 'That's my life # It's a invalid syntax, you must use an scape
string = 'That\'s my life' # or use "" double quotes
print(type(a))


#  03 - Operators (operadores)
# soma +
# menos -
# vezes *
# módulo %
n1 = 20 
n2 = 30
print(n1+n2)
print(n1-n2)
print(n1/n2)
print(n1*n2)

s1 = "Murilo"
s2 = "100"
print(s1+s2) # Concatenação
# print(s1=s2)
# print(s1/s2)
# print(s1*s2)
print(n2+s2)


parte1 = "Maratona"
parte2 = "Python"
completo = parte1 + parte2
print(completo)


#conversões
print("Murilo" + str(n2))

print(10 +int("30"))

#################################################################
#  02 - Lists and Tuples
#################################################################
# Lists (listas) *Sequence type
#  Listas são iguais caixas, mas como salvar o nome de 100 alunos em uma única variável?
aluno001 = "Murilo"
aluno002 = "Chico" # ...
# or better
# or better 
students = ["Murilo", "Chico", "Bruno", "Gio"] # [ is the list start\\ the "," is the delimiter, and list end] 
# como acessasr os elemntos de uma lista
print(students[0]) #começando por 0
# Por que? Imagina uma regúa, ela começa do 0 e não do 1, por isso!
print(students[-1])

# Como fazer se aparece um aluno novo?
# How to add an element into a list in python?
students.append("Jorge")

novo_aluno = "max"

students.append(novo_aluno)


print(students)

students.pop()

students.pop()
# Agora quantos alunos tem na sala?
len(students)

students.reverse()
print(students)
# Now what if...
print(students.reverse()) # None

print(type(students))

#Tuple
days = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(type(days))

print("Murilo" in students)


print("Mon" not in days)

#################################################################
#  03 - Dicts
#################################################################

N2 = {1, 2,3,4}
print(type(N2))


aluno = {
    "Nome": "Jorge",
    "Idade": 28,
    "brazil": True,
    "fav_foods":["pizza", "cachorro-quente"]
}

print(type(aluno))


print(aluno["Nome"])

print(aluno["Idade"])

aluno["Score"] = 100
print(aluno)

aluno.keys()


aluno.values()

alunos = [
    {"Nome": "Jorge","Idade": 28, "brazil": True,"fav_foods":["pão", "cachorro-quente"]},
    {"Nome": "Caio","Idade": 35, "brazil": False,"fav_foods":["bolo", "pão de queijo"]},
    {"Nome": "matheus","Idade": 37, "brazil": True,"fav_foods":["pizza", "feijão"]},
    {"Nome": "Lucas","Idade": 18, "brazil": True,"fav_foods":["arroz", "noz"]},
    {"Nome": "Marcos","Idade": 22, "brazil": True,"fav_foods":["panqueca", "cachorro-quente"]}
]
print(type(alunos))

print(aluno["Nome"])

for aluno in alunos:
  print(aluno["Nome"])
  print(aluno["Idade"])
  print(aluno['fav_foods'][0])
  print("------------------------")


#################################################################
#  04 - Built in Functions
#################################################################

import this