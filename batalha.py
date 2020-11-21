#Status do monstrinho 1
atk1 = int(input()) # Valor de ataque
def1 = int(input()) # Valor de defesa

#Status do monstrinho 2
atk2 = int(input()) # Valor de ataque
def2 = int(input()) # Valor de defesa

'''Verifica se o ataque e a defesa do
   oponente são iguais, e redefine o
   valor para a variável de ataque'''

atk1 = atk1 if not atk1 == def2 else 0
atk2 = atk2 if not atk2 == def1 else 0

'''Verifica se apenas uma das variáveis
   tem o valor de ataque maior que zero
   e caso sim, verifica e mostra se foi
   o jogador 1 ou 2 o vencedor, caso não
   printa -1'''

if((atk1 > 0 and atk2 == 0) or (atk2 > 0 and atk1 == 0)):
  if(atk1 > atk2):
    print(1)
  else:
    print(2)
else:
  print(-1)
