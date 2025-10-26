from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг
    def test_add_new_book_add_two_books(self):
        # создаем экземпляр (объект) класса BooksCollector
        collector = BooksCollector()

        # добавляем две книги
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_rating, который нам возвращает метод get_books_rating, имеет длину 2
        assert len(collector.get_books_rating()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()
       
    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Гарри Поттер', 'Фантастика'),
            ('Шерлок Холмс', 'Детективы'),
            ('Сияние', 'Ужасы'),
            ('Шрек', 'Мультфильмы'),
            ('Двенадцать стульев', 'Комедии')
        ]
    )
    def test_set_book_genre_valid_input_genre_assigned(self, name, genre):
        collector = BooksCollector()

        # Добавляем книгу и устанавливаем корректный жанр
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        # Проверяем, что жанр установлен корректно
        assert collector.books_genre[name] == genre


    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Властелин колец', 'Фантастика'),
            ('Шерлок Холмс', 'Детективы'),
            ('Сияние', 'Ужасы'),
            ('Шрек', 'Мультфильмы'),
            ('Двенадцать стульев', 'Комедии')
        ]
    )
    def test_get_book_genre_existing_book_returns_correct_genre(self, name, genre):
        collector = BooksCollector()

        # Добавляем книгу и задаем жанр
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        # Проверяем, что метод возвращает правильный жанр
        assert collector.get_book_genre(name) == genre


    def test_get_books_with_specific_genre_fantasy_return_all_matching_books(self):
        collector = BooksCollector()

        books = ['Гарри Поттер', 'Властелин колец', 'Дюна']
        genre = 'Фантастика'

        # Добавляем книги с жанром "Фантастика"
        for name in books:
            collector.add_new_book(name)
            collector.set_book_genre(name, genre)

        # Получаем список книг с жанром "Фантастика"
        books_in_genre = collector.get_books_with_specific_genre(genre)

        # Проверяем, что все добавленные книги вернулись
        assert books_in_genre == books
 

    def test_get_books_genre_new_collector_returns_empty_dict(self):
        collector = BooksCollector()

        # Проверяем, что у нового объекта словарь пуст
        assert collector.get_books_genre() == {}


    @pytest.mark.parametrize(
        'name, genre',
        [
            ('Гарри Поттер', 'Фантастика'),
            ('Шрек', 'Мультфильмы'),
            ('Винни-Пух и все, все, все', 'Комедии')
        ]
    )
    def test_get_books_for_children_books_with_allowed_genres_in_list(self, name, genre):
        collector = BooksCollector()

        # Добавляем книгу с "безопасным" жанром
        collector.add_new_book(name)
        collector.set_book_genre(name, genre)

        # Проверяем, что книга попала в список детских
        assert name in collector.get_books_for_children()


    def test_add_book_in_favorites_new_book_added(self):
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Гарри Поттер')

        # Добавляем книгу в избранное дважды
        collector.add_book_in_favorites('Гарри Поттер')

        # Проверяем, что книга в списке избранных
        favorites = collector.get_list_of_favorites_books()
        assert 'Гарри Поттер' in favorites

        
    def test_add_book_in_favorites_book_already_in_favorites_not_added(self):
        collector = BooksCollector()

        # Добавляем книгу
        collector.add_new_book('Шерлок Холмс')

        # Добавляем книгу в избранное дважды
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')

        # Проверяем, что книга в списке избранных только один раз
        favorites = collector.get_list_of_favorites_books()
        assert favorites.count('Шерлок Холмс') == 1


    def test_delete_book_from_favorites_book_in_favorites_book_removed(self):
        collector = BooksCollector()

        # Добавляем книгу и добавляем ее в избранное
        collector.add_new_book('Шерлок Холмс')
        collector.add_book_in_favorites('Шерлок Холмс')

        # Удаляем книгу из избранного
        collector.delete_book_from_favorites('Шерлок Холмс')

        # Проверяем, что её больше нет в списке избранных
        favorites = collector.get_list_of_favorites_books()
        assert 'Шерлок Холмс' not in favorites


    def test_get_list_of_favorites_returns_all_favorite_books(self):
        collector = BooksCollector()

        # Добавляем книги 
        collector.add_new_book('Шерлок Холмс')
        collector.add_new_book('Десять негритят')

        # Добавляем обе книги в избранное
        collector.add_book_in_favorites('Шерлок Холмс')
        collector.add_book_in_favorites('Десять негритят')

        # Проверяем, что список избранных содержит обе книги
        assert collector.get_list_of_favorites_books() == ['Шерлок Холмс', 'Десять негритят']
