##################################
# 05 functions (Funções)
##################################
# Sequência de códigos e comandos
# Escreve uma vez e pode ser reusalve, felixvel e modular. 
# f(x) = x2
# name - input - output , mas a função não precisa ter output necessariamente
#########
# Anatomia de uma função
# Toda a vez que um aluno entrar no site precisa constar o nome dele, como fazer isso dentro de uma função?
def welcome(name):
  welcome_msg = "olá" +" "+ name
  print(welcome_msg)
welcome("Murilo")

student = "Murilo"
# primeiro exemplo
def welcome(name): 
  #: <- é um escopo de código
  print("Estou dentro da função")
print('Estou fora da função')

welcome(student)
 
def welcome(name):  
  msg = "Olá" + name.capitalize()
  #capitalize só na primeira str
  print(msg)
welcome(student)
welcome("Lucas dos Santos")
welcome("Jorge Silva Matos")


def welcome(name):  
  msg = "Olá"   + name.title()
  #capitalize só na primeira str
  print(msg)
welcome(student)
welcome("Lucas dos Santos")
welcome("Jorge Silva Matos")

def plus(n1, n2):
  print(n1+n2)
  
def minus(n1, n2):
  print(n1-n2)

n1 = input("Digite o n1")
n2 = input("Digite o n2")
#input salve do tipo str, precisa arrumar 
plus(n1, n2)

def plus(n1, n2):
  print(n1+n2)
  
def min(n1, n2):
  print(n1-n2)

n1 = int(input("Digite o n1"))
n2 = int(input("Digite o n2"))

plus(n1, n2)

def plus(n1, n2=0): # definir valores nos argumentos
  print(n1+n2)
  
def minu(n1, n2):
  print(n1-n2)
plus

def welcomer(name = "anonymous"):
  print("Olá" + name)
welcome()


def welcome(name = "anonymous"):
  print(f"Olá usuário:"(name))

##################################
# 05 functions (Funções)
##################################
# input e output 
def plus (n1, n2):
  print(n1 + n2)
plus(10, 20 )

def p_plus(n1, n2):
  print(n1+n2)

def r_plus(n1, n2):
  total = n1 + n2
  return  total

p_result = p_plus(10,20)
r_result = r_plus(10,20)

print(p_plus, r_result)


def r_plus(n1, n2):
  total = n1 + n2
  return  total
  print("woooooow")

# under the return there is no life

def welcome(name, email, id):
  msg= f"Olá {name}, seu email é {email} e seu id é {id}  "
  return msg
# positional argument
print(welcome(od = 1137, email="eu@murilo.com", name="Murilo"))