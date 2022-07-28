# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. 
# Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. 
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, 
# чтобы забрать все конфеты у своего конкурента?
#   a) Добавьте игру против бота
#   b) Подумайте как наделить бота ""интеллектом""


from os import system
from pickle import FALSE, TRUE
from random import randint




def winning_condition (candies: int):
    is_candies = TRUE
    if candies > 0:
        is_candies = FALSE
    return is_candies

def player_turnf (current_player, candies: int):
    player_turn = int(input(f'{current_player}, Ваш ход. Сколько конфет забираешь. Не более 28? --> '))
    while (player_turn > 28) | (player_turn < 1):
        player_turn = int(input(f'{current_player}, Количество конфет должно быть от 0 до 28? --> '))
    candies -= player_turn
    print(f'Осталось {candies} конфет')
    if winning_condition(candies) is TRUE:
        print(f'Поздравляем! Победил {current_player}')
    return candies

def bot_turnf (candies: int):
    if candies <= 28:
        bot_turn = candies
    else:
        bot_turn = candies % 29  
        if bot_turn == 0:
            bot_turn = 1
    print(f'Бот берет {bot_turn} конфет')
    candies -= bot_turn
    print(f'Осталось {candies} конфет')
    if winning_condition(candies) is TRUE:
        print(f'Вы проиграли! А бот победил))')
    return candies

system('cls')
print("Игра в конфеты")
print('Правила игры: На столе 2021 конфета. \nИгроки берут по-очереди от 1 до 28 конфет.\nКто забирает последнюю - побеждает!')
print()
first_player = input('Ваше имя --> ')
print()
print(f'Приветствую, землянин {first_player}, с кем будем играть?')
print('1. Другой игрок')
print('2. Бот')
count_players = int(input('--->'))
while (count_players < 1) | (count_players > 2):
    count_players = int(input('Еще разок --->'))  

bot_player = 'БОТ'
if count_players == 1:
    second_player = input('Второй игрок, Ваше имя -->')
else:
    second_player = bot_player

gambling = None
check_gambling = None
print(f'Разыграем первый ход. {first_player},')
print()
while (gambling != 0) and (gambling != 1):
    gambling = int(input('Орел(1) или решка(0)?'))
    check_gambling = randint(0,1)
    print(f'Выпало {check_gambling}')
if gambling == check_gambling:
    print('Ура! Вы начинаете.')
    current_player = first_player
else:
    current_player = second_player
    print(f'Начинает {second_player}.')

candies = 50                  # Для проверки лучше уменьшить количество конфет))
while candies > 0:
    if current_player == bot_player:
        candies = bot_turnf(candies)
    else:
        candies = player_turnf(current_player, candies)
    
    print()
    
    if current_player == first_player:
        current_player = second_player
    else:
        current_player = first_player
