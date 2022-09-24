class ListExercise:
    @staticmethod
    def replace(input_list: list[int]) -> list[int]:
        """
        Заменить все положительные элементы целочисленного списка на максимальное значение
        элементов списка.
        :param input_list: Исходный список
        :return: Список с замененными элементами
        """
        maximum = 0
        for i in input_list:
            if i > maximum:
                maximum = i

        copy = input_list[::]

        for i in range(len(copy)):
            if copy[i] > 0:
                copy[i] = maximum

        return copy

    @staticmethod
    def search(input_list: list[int], query: int) -> int:
        """
        Реализовать двоичный поиск
        Функция должна возвращать индекс элемента
        :param input_list: Исходный список
        :param query: Искомый элемент
        :return: Номер элемента
        """

        def recursive_search(input_list: list[int], start: int, end: int, query: int) -> int:
            if start > end:
                return -1

            guess = (end + start) // 2

            if input_list[guess] == query:
                return guess
            elif input_list[guess] > query:
                return recursive_search(input_list, start, guess - 1, query)
            else:
                return recursive_search(input_list, guess + 1, end, query)

        return recursive_search(input_list, 0, len(input_list) - 1, query)
