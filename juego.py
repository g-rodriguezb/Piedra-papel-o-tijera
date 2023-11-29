# juego de piedra papel o tijeras

import random as rd

options = ('piedra', 'papel', 'tijera')

rounds = int(input('Mínimo de rondas ganadas para definir ganador: '))

if not rounds > 0:
  print('El valor ingresado no es válido. Por favor, ingresa un valor mayor a 0')

user_score = 0
computer_score = 0
counter_round = 1

while user_score < rounds and computer_score < rounds:

  print('*' * 10)
  print('ROUND ' + str(counter_round))
  print('*' * 10)
  
  user_option = input('piedra, papel o tijera => ').lower()
  computer_option = rd.choice(options)
  
  
  if not user_option in options:
    print('no es una opción válida')
    continue
  elif user_option == computer_option:
    print(f'Empate, la computadora eligió {computer_option} igual que tú')
    
  elif user_option == 'piedra' and computer_option == 'papel':
    print(f"Perdiste, la computadora eligió {computer_option}, y {computer_option} le gana a {user_option}")
    computer_score += 1
  
  elif user_option == 'papel' and computer_option == 'tijera':
    print(f"Perdiste, la computadora eligió {computer_option}, y {computer_option} le gana a {user_option}")
    computer_score += 1
    
  elif user_option == 'tijera' and computer_option == 'piedra':
    print(f"Perdiste, la computadora eligió {computer_option}, y {computer_option} le gana a {user_option}")
    computer_score += 1
    
  else:
    print(f"Ganaste, la computadora eligió {computer_option}, y {user_option} le gana a {computer_option}")
    user_score += 1
  print('-'*50)
  print(f'Puntuación actual: Usuario: {user_score} - Computadora: {computer_score}')
  print('-'*50)
  counter_round += 1


if user_score > computer_score:
  if rounds > 1:
    result = f'| Felicidades, ganaste las {rounds} rondas |'
  else:
    result ='| Felicidades, ganaste la ronda |'
else:
  if rounds > 1:
    result = f'| Has perdido las {rounds} rondas |'
  else:
    result = '| Has perdido la ronda |'

stars = len(result) - 2

print('*')
print('','-'*stars)
print(result)
print('','-'*stars)