from random import *

def joKenPo(player, computer, items):
    if player == 0 and computer == 1:
        return print(f'O computador venceu ! Você jogou: {items[player]}, o computador jogou: {items[computer]}')
    elif player == 1 and computer == 2:
        return print(f'O computador venceu ! Você jogou: {items[player]}, o computador jogou: {items[computer]}')
    elif player == 2 and computer == 0:
        return print(f'O computador venceu ! Você jogou: {items[player]}, o computador jogou: {items[computer]}')
    elif computer == 0 and player == 1:
        return print(f'Você venceu ! Você jogou: {items[player]}, o computador jogou: {items[computer]}')
    elif computer == 1 and player == 2:
        return print(f'Você venceu ! Você jogou: {items[player]}, o computador jogou: {items[computer]}')
    elif computer == 2 and player == 0:
        return print(f'Você venceu ! Você jogou: {items[player]}, o computador jogou: {items[computer]}')
    elif computer == jogador:
        return print(f'O jogo empatou ! Você jogou: {items[player]}, o computador jogou: {items[computer]}')
    else:
        return print(f'Jogada inválida ! Digite apenas: 0, 1 ou 2.')

jogadas = ('Pedra', 'Papel', 'Tesoura')
jogador = int(input("Digite a sua opção (pedra - 0, papel - 1 ou tesoura - 2): "))
computador = randint(0, 2)

joKenPo(jogador, computador, jogadas)