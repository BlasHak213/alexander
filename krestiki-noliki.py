import requests
import bs4
import time


krest_nol = [[" " for _ in range(3)] for _ in range(3)]

print(krest_nol)

def pole():
   for row in krest_nol:
      print("|".join(row))
      print("-----")

def win(symbol):
   for i in range(3):
      if krest_nol[i][0] == krest_nol[i][1] == krest_nol[i][2] == symbol:
         return True
      if krest_nol[0][i] == krest_nol[1][i] == krest_nol[2][i] == symbol:
         return True
   if krest_nol[0][0] == krest_nol[1][1] == krest_nol[2][2] == symbol:
      return True
   if krest_nol[0][2] == krest_nol[1][1] == krest_nol[2][0] == symbol:
      return True
   return False

player = 'X'

while True:
   pole()
   move = input(f'Игрок {player} введите координаты хода')
   stroka, stolb = map(int, move.split())
   if krest_nol[stroka-1][stolb-1] == " ":
      krest_nol[stroka-1][stolb-1] = player
   else:
      print('Эта клетка занята')
      continue

   if win(player):
      pole()
      print(f'Игрок {player} победил')
      break

   if all(all(kletka != " " for kletka in row) for row in krest_nol):
      pole()
      print('Ничья')
      break

   player = "O" if player == "X" else "X"

