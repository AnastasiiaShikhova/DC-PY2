import doctest


class Microscope:
    def __init__(self, eyepiece_fov: int, objectives_count: int, nosepiece: int):
        '''
        Создание объекта "Микроскоп"
        :param eyepiece_fov: Поле зрения окуляров
        :param objectives_count: Количество объективов
        :param nosepiece: Количество позиций в револьвере объективов

        Пример:
        >>> microscope = Microscope(22, 5, 6)
        '''

        if not isinstance(eyepiece_fov, (int)):
            raise TypeError("Значение поля зрения является целым числом")
        if eyepiece_fov <= 0:
            raise ValueError("Значение поля зрения не отрицательное")
        self.eyepiece_fov = eyepiece_fov

        if not isinstance(objectives_count, (int)):
            raise TypeError("Количество объективов должно быть целым числом")
        if objectives_count <= 0:
            raise ValueError("Количество объективов микроскопа не отрицательное")
        self.objectives_count = objectives_count

        if not isinstance(nosepiece, (int)):
            raise TypeError("Количество позиций в револьвере должно быть целым числом")
        if nosepiece <= 0:
            raise ValueError("Количество позиций в револьвере микроскопа не отрицательное")
        self.nosepiece = nosepiece

    def fov_w_objective(self, objective_magnification: float) -> int:
        '''
        Расчёт поля зрения микроскопа для конкретного объектива

        :param objective_magnification: Увеличение объектива
        :return: Поле зрения с объективом данного увеличения

        Пример:
        >>> microscope = Microscope(22, 5, 6)
        >>> microscope.fov_w_objective(4)
        '''
        if not isinstance(objective_magnification, (int, float)):
            raise TypeError("Увеличение объектива должно быть типа int или float")
        if objective_magnification <= 0:
            raise ValueError("Увеличение объектива не отрицательное")
        ...
    def add_objectives(self, added_objectives_count: int) -> int:
        '''
        Добавление объективов к микроскопу

        :param added_objectives_count: Количество добавляемых объективов
        :raise ValueError: Если количество добавляемых объективов превышает кольчество мест в револьвере с учётом уже имеющихся объективов, возвращается ошибка
        :return: Количество объективов, которое можно добавить

        Пример:
        >>> microscope = Microscope(22, 3, 6)
        >>> microscope.add_objectives(2)
        '''
        if not isinstance(added_objectives_count, (int)):
            raise TypeError("Количество объективов должно быть целым числом")
        if added_objectives_count <= 0:
            raise ValueError("Количество объективов не отрицательное")
        ...

class Game:
    def __init__(self, min_players: int, max_players: int):
        '''
        Создание объекта "Игра"
        :param min_players: минимальное необходимое количество игроков
        :param max_players: максимальное возможное количество игроков

        Пример:
        >>> game = Game(2, 10)
        '''
        if not isinstance(min_players, (int)):
            raise TypeError("Количество игроков должно быть целым числом")
        if min_players <= 1:
            raise ValueError("Минимальное количество игроков не менее одного")
        self.min_players = min_players

        if not isinstance(max_players, (int)):
            raise TypeError("Количество игроков должно быть целым числом")
        if max_players <= 1:
            raise ValueError("Махимальное количество игроков не менее одного")
        self.max_players = max_players

    def play_in_company(self, number_of_players: int) -> bool:
        '''
        Определение, может ли задаваемое количество игроков сыграть в игру

        :param number_of_players: Количество игроков
        :raise ValueError: Количество игроков меньше минимально возможного количества игроков - ошибка "Недостаточно игроков"
        :raise ValueError: Количество игроков больше максимально возможного количества игроков - ошибка "Перебор игроков"
        :return: True, если количество игроков удовлетворяет условию

        Пример:
        >>> game = Game(2, 10)
        >>> game.play_in_company(7)
        '''
        if not isinstance(number_of_players, (int)):
            raise TypeError("Количество игроков должно быть целым числом")
        if number_of_players <= 1:
            raise ValueError("Количество игроков не менее одного")
        ...

    def play_in_comand(self, number_of_players: int) -> int:
        '''
        Могут ли игроки разделиться на команды поровну
        :param number_of_players: Количество игроков
        :raise ValueError: Количество игроков не позволяет разделиться на команды поровну
        :return: Максимальное число команд, на которые могут разделиться игроки поровну

        Пример:
        >>> game = Game(2, 10)
        >>> game.play_in_comand(3)
        '''
        if not isinstance(number_of_players, (int)):
            raise TypeError("Количество игроков должно быть целым числом")
        if number_of_players <= 1:
            raise ValueError("Количество игроков не менее одного")
        ...

class HolydayHomerwork:
    def __init__(self, task_count: int, holydays: int):
        '''
        Создание объекта "Задания на каникулы"
        :param task_count: Количество заданий
        :param holydays: Количество дней каникул

        Пример:
        >>> holyday_homework = HolydayHomerwork(81, 11)
        '''
        if not isinstance(task_count, (int)):
            raise TypeError("Количество заданий должно быть целым числом")
        if task_count <= 0:
            raise ValueError("Количество заданий не отрицательное")
        self.task_count = task_count
        if not isinstance(holydays, (int)):
            raise TypeError("Количество дней должно быть целым числом")
        if holydays <= 0:
            raise ValueError("Количество дней не отрицательное")
        self.holydays = holydays

    def count_of_daily_tasks(self, current_day: int) -> int:
        '''
        Определение количества заданий, которые надо выполнять ежедневно
        :param current_day: Количество дней, прошедших с начала каникул
        :return: Минимальное число заданий, которое нужно выполнять каждый день до конца каникул

        Пример:
        >>> holyday_homework = HolydayHomerwork(81, 11)
        >>> holyday_homework.count_of_daily_tasks(2)
        '''
        if not isinstance(current_day, (int)):
            raise TypeError("Количество дней быть целым числом")
        if current_day <= 0:
            raise ValueError("Количество дней не отрицательно")
        ...

    def count_of_days(self, completed_tasks: int) -> int:
        '''
        Определение количества дней для решения заданного количества заданий
        :param completed_tasks: Количество заданий, которые выполняются ежедневно
        :raise ValueError: Количество дней для выполнения заданий превышает количество дней каникул
        :return: Количество дней, за которые будут решены все задания

        Пример:
        >>> holyday_homework = HolydayHomerwork(81, 9)
        >>> holyday_homework.count_of_days(10)
        '''
        if not isinstance(completed_tasks, (int)):
            raise TypeError("Количество заданий быть целым числом")
        if completed_tasks <= 1:
            raise ValueError("Количество заданий не менее одного")
        ...
if __name__ == "__main__":
    doctest.testmod()

