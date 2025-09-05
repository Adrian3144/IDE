"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""
import numpy as np

def random_predict(number:int=1) -> int:
    """ Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101) # предполагаемое число
        
        if number == predict_number:
            break # выход из цикла если угадали
        
    return count


def score_game(random_predict) -> int:
    """За какое количество попыток в среднем угадывает за 1000 наш алгоритм 

    Args:
        random_predict (_type_): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    np.random.seed(1) # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=1000) # загадали список чисел
    
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    print(f'Ваш алгоритм угадывает число в среднем за {score} попыток')
    return score


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    right_side = 200
    left_side = 1

    while True: # Цикл While генерит случанйые цифры в диапазоне от right_side и left_side
      random_array = np.random.randint(left_side, right_side)
      count += 1

      if number > random_array: # Если случайное число меньше загадонного, то приравниваем леву границу этому числу
        left_side = random_array
      elif number < random_array: # Если случайное число больше загадонного, то приравниваем правую границу этому числу
        right_side = random_array
      else: # Иначе компьютер угадал. Выход из цикла
        break

    return count


if __name__ == "__main__":
    score_game(random_predict)