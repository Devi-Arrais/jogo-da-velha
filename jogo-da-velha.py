import random
import os
jogadas = 0
player = 1
vitoria = False
velha = [
         [" ", " ", " "],
         [" ", " ", " "],
         [" ", " ", " "]
          ]

def tela():
   global velha
   global jogadas
   os.system("clear")
   print(f"{velha[0][0]} | {velha[0][1]} | {velha[0][2]}")
   print("---------")
   print(f"{velha[1][0]} | {velha[1][1]} | {velha[1][2]}")
   print("---------")
   print(f"{velha[2][0]} | {velha[2][1]} | {velha[2][2]}")
   print("Jogadas: " + str(jogadas))

def quemJoga():
   global jogadas
   global player
   #global vitoria
   if player == 1 and jogadas <= 9:
      try:
         ln = int(input("Linha: "))
         cl = int(input("Coluna: "))
         while velha[ln][cl] != " ":
            ln = int(input("Linha: "))
            cl = int(input("Coluna: "))
         velha[ln][cl] = "X"
         player = 2
         jogadas += 1
      except:
         print("Linha ou coluna invalida")
def cpu():
   global jogadas
   global player
   if player == 2 and jogadas <= 9:
      ln = random.randrange(0, 3)
      cl = random.randrange(0, 3)
      while velha[ln][cl] != " ":
         ln = random.randrange(0, 3)
         cl = random.randrange(0, 3)
      velha[ln][cl] = "O"
      jogadas += 1
      player = 1

def vitoria():
   global vitoria
   if (velha[0][0] == "X") and (velha[0][1] == "X") and (velha[0][2] == "X"):
      vitoria = True
      print("Você ganhou!!!")
   elif (velha[1][0] == "X") and (velha[1][1] == "X") and (velha[1][2] == "X"):
      vitoria = True
      print("Você ganhou!!!")
   elif (velha[2][0] == "X") and (velha[2][1] == "X") and (velha[2][2] == "X"):
      vitoria = True
      print("Você ganhou!!!")
   elif (velha[0][0] == "X") and (velha[1][0] == "X") and (velha[2][0] == "X"):
      vitoria = True
      print("Você ganhou!!!")
   elif (velha[0][1] == "X") and (velha[1][1] == "X") and (velha[2][1] == "X"):
      vitoria = True
      print("Você ganhou!!!")
   elif (velha[0][2] == "X") and (velha[1][2] == "X") and (velha[2][2] == "X"):
      vitoria = True
      print("Você ganhou!!!")
   elif (velha[0][0] == "X") and (velha[1][1] == "X") and (velha[2][2] == "X"):
      vitoria = True
      print("Você ganhou!!!")
   elif (velha[0][2] == "X") and (velha[1][1] == "X") and (velha[2][0] == "X"):
      vitoria = True
      print("Você ganhou!!!")
   elif (velha[0][0] == "O") and (velha[0][1] == "O") and (velha[0][2] == "O"):
      vitoria = True
      print("A CPU ganhou!")
   elif (velha[1][0] == "O") and (velha[1][1] == "O") and (velha[1][2] == "O"):
      vitoria = True
      print("A CPU ganhou!")
   elif (velha[2][0] == "O") and (velha[2][1] == "O") and (velha[2][2] == "O"):
      vitoria = True
      print("A CPU ganhou!")
   elif (velha[0][0] == "O") and (velha[1][0] == "O") and (velha[2][0] == "O"):
      vitoria = True
      print("A CPU ganhou!")
   elif (velha[0][1] == "O") and (velha[1][1] == "O") and (velha[2][1] == "O"):
      vitoria = True
      print("A CPU ganhou!")
   elif (velha[0][2] == "O") and (velha[1][2] == "O") and (velha[2][2] == "O"):
      vitoria = True
      print("A CPU ganhou!")
   elif (velha[0][0] == "O") and (velha[1][1] == "O") and (velha[2][2] == "O"):
      vitoria = True
      print("A CPU ganhou!")
   elif (velha[0][2] == "O") and (velha[1][1] == "O") and (velha[2][0] == "O"):
      vitoria = True
      print("A CPU ganhou!")

while True:
   tela()
   quemJoga()
   cpu()
   vitoria()
   if (vitoria == True):
      break
