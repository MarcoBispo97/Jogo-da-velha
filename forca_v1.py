# -*- coding: utf-8 -*-

#Hangman game (Jogo da forca)
#Programação Orientada a Objetos


#Import
import random
# tabuleiro
#Lista para fazer a animação

board = ['''

>>>>>>>>>>>>>>Hangman<<<<<<<<<<<<<<<<<
         
         +------+
         |      |
                |
                |
                |
                |
                |
         ================''','''
         +------+
         |      |
         0      |
                |
                |
                |
                |
         ================'''
         '','''
         +------+
         |      |
         0      |
         |      |
                |
                |
                |
         ================''','''
         +------+
         |      |
         0      |
         |\     |
                |
                |
                |
         ================''','''
         +------+
         |      |
         0      |
        /|\     |
                |
                |
                |
         ================''','''
         +------+
         |      |
         0      |
        /|\     |
        /       |
                |
                |
         ================''','''
         +------+
         |      |
         0      |
        /|\     |
        / \     |
                |
                |
         ================''']

#Classe
class Hangman:

    #Método construtor
    def __init__(self,word):
        self.word = word #definiu que  vai ter uma palavra no projeto
        self.missed_letters = [] #foi criado duas listas letras erradas e certas
        self.guessed_letters = []


    #Método para adivinhar a letra
    def guess(self, letter):
        if letter in self.word and letter not in self.guessed_letters: #se a letra dentro da palavra não estiver
            self.guessed_letters.append(letter) #dentro da palavra certa e a letra não estiver na lista append
        elif letter not in self.word and letter not in self.missed_letters:
            self.missed_letters.append(letter)
        else:
            return False
        return True

    # Método para verificar se o jogo terminou
    def hangman_over(self):
        return self.hangman_won() or (len(self.missed_letters) == 6)
    #Quando o jogo termina, se ele venceu ou perdeu com 6 tentativas

    #Método para verificar se o jogador venceu
    def hangman_won(self):
        if '_' not in self.hide_word():
            return True
        return False


    #Método para não mostrar a letra no board
    def hide_word(self):
        rtn = ''
        for letter in self.word: #para cada letra da sequencia de letras, se a letra estiver na palavra preeenche
            if letter not in self.guessed_letters: #se não tiver _
                rtn += '_'
            else:
                rtn += letter
        return rtn

    #Método para checar o status do game e imprimir o board na tela
    def print_game_status(self):
        print(board[len(self.missed_letters)]) #board é uma lista, posso acessa cada posição dela
        print('\nPalavras:'+ self.hide_word()) #board[1] estou buscando a segunda posição da lista
        print('\nLetras erradas:',)
        for letter in self.missed_letters:
            print(letter,)
        print()
        print('Letras corretas: ',)
        for letter in self.guessed_letters:
            print(letter,)
        print()

#Função para ler uma palavra de forma aleatória do banco de palavras
def rand_word():
    with open("palavras.txt", "rt") as f:
        bank = f.readlines()
    return bank[random.randint(0, len(bank))].strip()

#Método Main - Execução do Programa
def main():
    #Objeto
    game = Hangman(rand_word())

    #Enquanto o jogo não estiver terminado, print no status, solicita uma letra e faz a leitura do caracter


    while not game.print_game_status():
        game.print_game_status()
        user_input = input('\nDigite uma letra:  ')
        game.guess(user_input)

    #Verifica o status do jogo
    game.print_game_status()

    #De acordo com o status, imprime mensagem na tela do usuário
    if game.hangman_won():
        print('\n Parabéns você venceu!!')
    else:
        print('\nGame over ! Você perdeu')
        print('A palavra era' + game.word)

    print('\nFoi bom jogar com você\n')

        #Executa o programa
if __name__ == "__main__":
    main()