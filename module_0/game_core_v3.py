#!/usr/bin/env python
# coding: utf-8

# In[37]:


import numpy as np
count = 0                            # счетчик попыток
number = np.random.randint(1,101)    # загадали число
#print ("Загадано число от 1 до 100", number)

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count+=1
        predict = np.random.randint(1,101) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1

    predict = np.random.randint(1,101)
    while number != predict:
        count+=1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    ''' аналог бинарного метода , только используется условие не "больше меньше" , а условие вхождения в диапазон'''
    
    # устанавливаем стартовые значений переменных для обработки диапазонов
    start_range = 0
    mid_range  = 25
    end_range = 50
    # строка для отладки кода print("начальные значения счетчиков",start_range,mid_range,end_range,"загаданное число",number)
    predict = 0
    magic = 100
    counter = 0
    
    # цикл для подсчета попыток 
    while number != predict:
        counter += 1 #счетчик попыток
    
    # основной алгоритм, делим диапазоны и сверяем наличие сгенерированого числа из диапазона 
    # на равенство загаданному компьютером
        
        if number in range(start_range,end_range):
            magic = end_range
            end_range = mid_range       
            #проверка последней итерации что бы исключить ошибку генерации из диапазона 
            if start_range >= end_range:  
                break
            # генерируем новое случайное число из диапазона в котором есть искомое число
            predict = np.random.randint(start_range,end_range)
            mid_range = start_range + (len(range(start_range, end_range)))//2
        else:
            # строка для отладки кода print(number,"не в диапазоне",start_range,end_range,"predict",predict)
            start_range = end_range + 1
            end_range = magic
            #проверка последней итерации что бы исключить ошибку генерации из диапазона 
            if start_range >= end_range:
                break
            # генерируем новое случайное число из диапазона в котором есть искомое число
            predict = np.random.randint(start_range,end_range)
            magic = end_range
            mid_range = start_range + (len(range(start_range, end_range)))//2
     
    return(counter)

def score_game(game_core):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за {score} попыток")
    return(score)

# запускаем
#score_game(game_core_v1)
#score_game(game_core_v2)
score_game(game_core_v3)


# In[ ]:





# In[ ]:




