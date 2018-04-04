"""
== Лото ==
Правила игры в лото.
Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.
Пример одного хода:
Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 87     - 14    11      
      16 49    55 88    77    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)
Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.
Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html
"""

import random
class Card():
    def __init__(self, card_holder):
        self.holder = card_holder
        self.rows = 3
        self.cols = 9
        self.num_in_rows = 5
        self.card = []
        self.row_indexes = [i for i in range(self.rows)]
        self.col_indexes = [i for i in range(self.cols)]
        self.counts_in_rows = [0 for i in self.row_indexes]
    def empty_card(self):
        card = []
        for i in range(self.rows):
            card.append([])
            for j in range(self.cols):
                card[i].append(' ')
        return card
    def generate_num(self):
        return random.randint(1,90)
    
    def generate_card(self):
        self.card = self.empty_card()
        while sum(self.counts_in_rows)<15:
            num = self.generate_num()
            num_col_index = (num-1)//10
            for row in self.row_indexes:
                if self.card[row][num_col_index] == num:
                    break
                elif self.card[row][num_col_index] == ' ' and self.counts_in_rows[row]<5:
                    self.card[row][num_col_index] = num
                    self.counts_in_rows[row] += 1
                    break
        return self.card
    
    def close_num(self, num):
        for row in self.row_indexes:
            for col in self.col_indexes:
                if num == self.card[row][col]:
                    self.card[row][col] = 'X'
                    self.counts_in_rows[row] -= 1
                    return self.card
        return self.card
    
    def num_in_card(self, num):
        for row in self.row_indexes:
            for col in self.col_indexes:
                if num == self.card[row][col]:
                    return True
        return False
    
    def __str__(self):
        string = '{}'.format(self.holder)+'-'*(29-len(self.holder))+'\n'
        for i in self.row_indexes:
            string += '|'
            for j in self.col_indexes:
                if len(str(self.card[i][j])) == 1:
                    string += ' '+str(self.card[i][j]) + ' '
                else:
                    string += str(self.card[i][j]) + ' '
            string +='|\n'
        string += '-'*29
        return string
class Loto():
    def __init__(self, player, computer):
        self.player = player
        self.computer = computer
    def out(self):
        print(self.player)
        print(self.computer)
    def start(self):
        pop = [i for i in range(1,91)]
        player = self.player
        computer = self.computer
        step = 0
        nums_already = ''
        for num in random.sample(pop, k = 90):
            step += 1
            nums_already += str(num) + ' '
            print('Ход №:', step)
            print('Номер бочонка:', num)
            print('Уже выпавшие бочонки:', nums_already)
            self.out()
            computer.close_num(num)
            ans = input('Зачеркнуть? y/n:')
            if ans == 'y' and player.num_in_card(num):
                player.close_num(num)
            elif ans == 'n' and player.num_in_card(num):
                print('Такой бочонок есть!{} програл!'.format(player.holder))
                break
            elif ans == 'n' and not player.num_in_card(num):
                player.close_num(num)
            elif ans == 'y' and not player.num_in_card(num):
                print('Такого бочонка нет!{} програл!'.format(player.holder))
                break
            if sum(player.counts_in_rows)==0 and sum(computer.counts_in_rows)==0:
                print('Ничья')
                break
            elif sum(player.counts_in_rows)==0:
                print('{} Выиграл!'.format(player.holder))
                break
            elif sum(computer.counts_in_rows)==0:
                print('{} Выиграл!'.format(computer.holder))
                break
            print('Следующий ход.')
            
if __name__ == '__main__':
    player = Card('Player')
    player.generate_card()

    computer = Card('Computer')
    computer.generate_card()

    loto = Loto(player, computer)
    loto.start()

