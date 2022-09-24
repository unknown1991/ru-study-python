from typing import Union


class MapExercise:
    @staticmethod
    def rating(list_of_movies: list[dict]) -> float:
        """
        !!Задание нужно решить используя map!!
        Посчитать средний рейтинг фильмов (rating_kinopoisk), у которых две или больше стран.
        Фильмы у которых рейтинг не задан или равен 0 не учитывать в расчете среднего.
        :param list_of_movies: Список фильмов.
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :return: Средний рейтинг фильмов у которых две или больше стран
        """
<<<<<<< Updated upstream
        pass
=======

        rating_sum = 0.0
        movies_count = 0

        for movie in list_of_movies:
            country_count = movie["country"].count(",") + 1
            movie_rating = movie["rating_kinopoisk"]

            if country_count > 1 and movie_rating != "" and float(movie_rating) > 0:
                rating_sum += float(movie["rating_kinopoisk"])
                movies_count += 1

        average_rating = rating_sum / movies_count

        return average_rating
>>>>>>> Stashed changes

    @staticmethod
    def chars_count(list_of_movies: list[dict], rating: Union[float, int]) -> int:
        """
        !!Задание нужно решить используя map!!
        Посчитать количество букв 'и' в названиях всех фильмов с рейтингом (rating_kinopoisk) больше
        или равным заданному значению
        :param list_of_movies: Список фильмов
        Ключи словаря: name, rating_kinopoisk, rating_imdb, genres, year, access_level, country
        :param rating: Заданный рейтинг
        :return: Количество букв 'и' в названиях всех фильмов с рейтингом больше
        или равным заданному значению
        """
<<<<<<< Updated upstream
        pass
=======

        filtered_list_of_movies = (
            movie["name"]
            for movie in list_of_movies
            if movie["rating_kinopoisk"] != "" and float(movie["rating_kinopoisk"]) >= rating
        )

        return sum(map(lambda name: name.count("и"), filtered_list_of_movies))
>>>>>>> Stashed changes
