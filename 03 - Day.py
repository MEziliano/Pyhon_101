###################
# Day 03
#################### 
# start -> do -> Do z-> Do y
def unlock_adult_movie(username, age):
  if age>=18:
    msg=f"{username} pode assitir filmes adultos"
  else:
    msg=f"{username} não pode assistir filmes adultos"
  
  return msg
# print(unlock_adult_movie("Luquihas", 12))
# print(unlock_adult_movie("Jorge", 18))
# print(unlock_adult_movie("Marcos", 25))

# Second example
def unlock_adlt_movie(username, age, with_parents):
  if age>=18:
    msg=f"{username} pode assitir filmes adultos"
  else:
    if with_parents:
      msg=f"{username} pode assitir filmes adultos, pois está com os pais"
    else:
      msg=f"{username} não pode assistir filmes adultos, sem os pais"
  
  return msg
  
# print(unlock_adlt_movie("Luquihas", 12, True))
# print(unlock_adlt_movie("Marquinhos",15, False))
# print(unlock_adlt_movie("luluzinha", 17, True))

def unlock_all_movie(username, age, with_parents):
  if age>=18:
    msg=f"{username} pode assitir filmes adultos"
  elif with_parents:
      msg=f"{username} pode assitir filmes adultos, pois está com os pais"
  else:
      msg=f"{username} não pode assistir filmes adultos, sem os pais"
  return msg
# Tudo é questão de lógica...
# print(unlock_all_movie("Luquihas", 12, True))
# print(unlock_all_movie("Marquinhos",15, False))
# print(unlock_all_movie("luluzinha", 17, True))
# Ou talvez
def unlock_a_movie(username, age, with_parents):
  if age>=18 or with_parents: # ou usar and
    msg=f"{username} pode assitir filmes adultos"
  else:
      msg=f"{username} não pode assistir filmes adultos, sem os pais"
  return msg

# print(unlock_all_movie("Luquihas", 12, True))
# print(unlock_all_movie("Marquinhos",15, False))
# print(unlock_all_movie("luluzinha", 17, True))

#######################################
#####--------For loop -------##########
#######################################
# for item in list:
#    --do--
#
students = [{"name": "murilo", "score":50},
  {"name": "josé", "score":25,},
  {"name": "joao", "score":37},{"name": "wade", "score":44},
  {"name": "wilson", "score":24}
]
# print(type(students))
# for student in students:
#   print(student)
#   print('#######')

# for student in students:
#   print(student["name"])
#   print(f'---------------')
# for student in students:
#   print(f" O aluno (a) student{['name']}tem nota [{'score'}]")


# for student in students:
#   score= student["score"]
#   if score < 50:
#     print(f"{student['name']} reprovou :(")
#     #Quando usar fstring usar '' nas variaveis
#   else:
#     print(f"O {student['name']} venceu! :)")

# winners = []
# reproved = []
# for student in students:
#   score= student["score"]
#   if score < 50:
#      reproved.append(student)
#   else:
#     winners.append(student)

# print(winners)
# print("----------------")
# print(reproved)
    
# winners = []
# reproved = []
# def list_winners_reproved(students):
#   for student in students:
#     score= student["score"]
#   if score < 50:
#      reproved.append(student)
#   else:
#     winners.append(student)
######################################
# For loop
######################################
# break
# for i in students:
#   if i["score"] <40:
#     break
#   else:
#     print(i['name'])

#continue
# for i in students:
#   if i["score"] <30:
#     continue
#   else:
#     print(i['name'])

# for i in students:
#   name_cap = i["name"].capitalize()
#   print(name_cap)



#########################
# ------- modules--------
#########################
# cada arquivo (main.py) é um módulo, que nada mais é que um conjunto de códigos. E esses arquivos se comunicam entre si. 