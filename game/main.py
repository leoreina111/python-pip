import random

def choice_options():
  options = ('piedra','papel','tijera')
  user_option = input('Pieda, papel o tijera --> ').lower()
  user_option = user_option.lower()
  computer_option = random.choice(options)
  print('computer_option = ',computer_option)
  
  if (not user_option in options):
    print('Opción no válida')
    #continue
    return None,None

  return user_option,computer_option

def check_rules(user_option,computer_option,cant_gano_user,cant_gano_computer):

  if (user_option == computer_option):
    print('Empate!')
  elif (user_option == 'piedra' and computer_option =="tijera"):
    print('piedra gana tijera: Gana User!')
    cant_gano_user += 1
  elif (user_option == 'piedra' and computer_option =="papel"):
    print('piedra gana papel: Gana Computer!')
    cant_gano_computer += 1
  elif (user_option == 'papel' and computer_option =="piedra"):
    print('papel gana piedra: Gana User!')
    cant_gano_user += 1
  elif (user_option == 'papel' and computer_option =="tijera"):
    print('papel pierde tijera: Gana Computer!')
    cant_gano_computer += 1
  elif (user_option == 'tijera' and computer_option =="piedra"):
    print('tijera pierde piedra: Gana Computer!')
    cant_gano_computer += 1
  elif (user_option == 'tijera' and computer_option =="papel"):
    print('tijera pierde papel: Gana User!')
    cant_gano_user += 1
  else:
    print('WTF!')

  return cant_gano_user,cant_gano_computer

def run_game():
  rounds = 1
  cant_gano_user = 0
  cant_gano_computer = 0
  
  while True:
    print('*' *10)
    print('ROUND ',rounds)
    print('*'*10)

    user_option, computer_option = choice_options()
    
    cant_gano_user, cant_gano_computer = check_rules(user_option,computer_option,cant_gano_user,cant_gano_computer)
  
    print('User wins = ',cant_gano_user)
    print('Computer wins = ',cant_gano_computer)

    if cant_gano_user == 2:
      print('GANÓ COMPUTER')
      break

    if cant_gano_computer == 2:
      print('GANÓ USER')
      break

    rounds = rounds + 1;

run_game()