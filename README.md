# qa_python

Тесты для `BooksCollector` (pytest).

Реализованы проверки:

- `test_add_new_book_adds_books_and_sets_empty_genre` — добавление книг и пустое значение жанра (`""`).
- `test_add_new_book_valid_boundary_name_lengths` — граничные валидные длины названия (1 и 40 символов), параметризация.
- `test_add_new_book_invalid_name_lengths_not_added` — невалидные длины названия (0 и 41 символ), параметризация.
- `test_add_new_book_duplicate_not_added_twice` — повторное добавление одной книги.
- `test_set_book_genre_sets_valid_genre` — установка допустимых жанров, параметризация.
- `test_set_book_genre_invalid_genre_not_set` — недопустимый жанр не устанавливается.
- `test_set_book_genre_for_nonexistent_book_does_nothing` — жанр не ставится для отсутствующей книги.
- `test_get_book_genre_returns_set_genre` — получение установленного жанра.
- `test_get_book_genre_returns_none_for_unknown_book` — `None` для отсутствующей книги.
- `test_get_books_with_specific_genre_returns_matching_books` — фильтрация по жанру, параметризация.
- `test_get_books_with_specific_genre_returns_empty_for_unknown_genre` — пустой список для неизвестного жанра.
- `test_get_books_genre_returns_current_dict` — возврат текущего словаря `books_genre`.
- `test_get_books_for_children_excludes_age_rated_genres` — книги для детей без возрастного рейтинга.
- `test_add_book_in_favorites_adds_existing_book` — добавление в избранное.
- `test_add_book_in_favorites_not_added_twice` — дубль в избранное не добавляется.
- `test_add_book_in_favorites_nonexistent_book_not_added` — книга вне словаря не попадает в избранное.
- `test_delete_book_from_favorites_removes_book` — удаление из избранного.
- `test_delete_book_from_favorites_unknown_book_not_removed` — удаление несуществующей книги не меняет список.
- `test_delete_book_from_favorites_empty_list_unchanged` — удаление из пустого списка.
- `test_get_list_of_favorites_books_returns_favorites_list` — возврат списка избранных книг.

Фикстура `collector` вынесена в `conftest.py`.

Запуск:
`pytest -v tests.py`
