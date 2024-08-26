import numpy as np
number = np.random.randint(1,101) #Загаданное число
print(f'Загаданное число {number}')
def random_predict(number: int) -> int:
    """ Рандомно угадываем число
    
    Args:
    number (int): Рандомное число от 1 до 100, загаданное компьютером

    Returns:
        int: Количество попыток
    """
    count = 0 #количество попыток
    range_max = 101 #Верхняя граница угадывания
    range_min= 1 #Нижняя граница угадывания
    
    while True:
        predict_number = np.random.randint(range_min,range_max) #Проверяемое число
        count += 1 #Количество попыток увеличивается на 1 с каждой итерацией цикла
        
        #Если загаданное число больше проверяемого - нижняя граница угадывания меняется 
        if number > predict_number:
            range_min = predict_number
            
        #Если загаданное число меньше проверяемого - верхняя граница угадывания меняется 
        elif number < predict_number:
            range_max = predict_number
            
        #Выход из цикла если угадали
        else:
            break
    return(count)

print(f'Количество попыток: {random_predict(number)}')

def score_game(random_predict) -> int:
    """За какое количество попыток в среднем из 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """

    count_ls = [] # список для сохранения количества попыток
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000)) # загадали список чисел
    
    #Цикл перебора загаданных чисел за 1000 раз внутри функции random_predict
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls)) # находим среднее количество попыток
    
    print(f'Ваш алгоритм угадывает число в среднем за: {score} попыток')
    return(score)
 #   
if __name__ == '__main__':
    
    score_game(random_predict)