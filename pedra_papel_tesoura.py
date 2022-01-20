import random as rd

lista = ['pedra', 'papel', 'tesoura']
sorteio = rd.choice(lista)

while True:
    jogada = input('Pedra, papel ou Tesoura? ').upper().lower()

    if jogada == 'pedra' or jogada == 'papel' or jogada == 'tesoura':
        print(f'Jogador 1: {jogada}')
        print(f'Bot: {sorteio}')

        # PEDRA COMO JOGADA FIXA
        if jogada == 'pedra' and sorteio == 'pedra':
            print('Empate!')
            break

        elif jogada == 'pedra' and sorteio == 'papel':
            print('Você PERDEU! :(')
            break

        elif jogada == 'pedra' and sorteio == 'tesoura':
            print('Parabéns, você VENCEU! :)')
            break

        # PAPEL COMO JOGADA FIXA
        elif jogada == 'papel' and sorteio == 'pedra':
            print('Parabéns, você VENCEU! :)')
            break

        elif jogada == 'papel' and sorteio == 'papel':
            print('Empate!')
            break

        elif jogada == 'papel' and sorteio == 'tesoura':
            print('Você PERDEU! :(')
            break

        # TESOURA COMO JOGADA FIXA
        elif jogada == 'tesoura' and sorteio == 'pedra':
            print('Você PERDEU! :(')
            break

        elif jogada == 'tesoura' and sorteio == 'papel':
            print('Parabéns, você VENCEU! :)')
            break

        elif jogada == 'tesoura' and sorteio == 'tesoura':
            print('Empate!')
            break

    else:
        print('Digite uma jogada válida!')
        continue