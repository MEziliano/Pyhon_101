import random
def create_password():
  lower    ="abcdefghijklmnopqrstuvwxyz"
  upper    ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
  number   = "0123456789"
  symbol   = "}{[]()*/;:_-#!@$£%¢&^~=+§\|><,."

  easy = lower+upper
  medium = lower+upper+number
  hard = lower+upper+symbol+number

  length   = int(input('Você quer uma senha com quantas letras\n'))  
  get_numbers  = str(input("Deseja números na sua senha?\n"))
  answer_numbers = get_numbers.lower()
  get_specials = str(input("E caracteres especiais?\n"))
  answer_specials = get_specials.lower()


  easy_password = "".join(random.sample(easy, length))
  middle_password = "".join(random.sample(medium, length))
  strong_password = "".join(random.sample(hard, length)) 

      
  if answer_numbers == "não": 
    print(easy_password)
  elif answer_specials == "não":
    print(middle_password)
  else:
    print(strong_password)


create_password()        