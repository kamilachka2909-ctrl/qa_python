# qa_python 
**Sprint_4**

**Реализованные тесты:**

test_add_new_book_add_two_books_books_count_is_two - метод add_new_book, добавление двух новых книг.
test_set_book_genre_valid_input_genre_assigned - методы set_book_genre, при передаче корректных данных жанр книги устанавливается и получаем словарь books_genre с указаанием жанра.
test_get_book_genre_existing_book_returns_correct_genre - методы get_book_genre, получаем словарь books_genre с жанром книги по её названию.
test_get_books_with_specific_genre_fantasy_return_all_matching_books - метод get_books_with_specific_genre, выводятся все добавленные книги в жанре фантастики.
test_get_books_genre_new_collector_returns_empty_dict - метод get_books_genre возвращает пустой словарь для нового объекта.
test_get_books_for_children_books_with_allowed_genres_in_list - метод get_books_for_children, если книга не принадлежит к жанру из возрастных ограничений, то она включается в список, возвращаемый методом.
test_add_book_in_favorites_new_book_added - метод add_book_in_favorites, новая книга добавляется в список избранных.
test_add_book_in_favorites_book_already_in_favorites_not_added - метод add_book_in_favorites, книга повторно не добавляется, если она уже есть в списке избранных.
test_delete_book_from_favorites_book_in_favorites_book_removed - метод delete_book_from_favorites_books, книга удаляется из списка избранных.
test_get_list_of_favorites_returns_all_favorite_books - метод get_list_of_favorites выводит список с избранными книгами.

