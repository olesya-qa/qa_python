# qa_python

Тесты для `BooksCollector` (pytest).

Реализованы проверки:

- `test_add_new_book_adds_books_and_sets_empty_genre` — добавление книг и пустое значение жанра (`""`).
- `test_add_new_book_rejects_invalid_names_and_duplicates` — отказ при пустом названии/слишком длинном названии (>40) и запрет повторного добавления.
- `test_set_book_genre_sets_only_for_existing_books_and_valid_genres` — установка жанра только для существующей книги и только для допустимых жанров.
- `test_get_book_genre_returns_genre_or_none` — получение жанра по названию (и `None` для отсутствующей книги).
- `test_get_books_with_specific_genre_filters_correctly` — фильтрация книг по жанру и возврат `[]` для неизвестного жанра.
- `test_get_books_genre_returns_current_dict` — возврат текущего словаря `books_genre`.
- `test_get_books_for_children_excludes_age_rated_genres` — книги для детей: жанры с возрастным рейтингом исключаются, также исключаются неустановленные жанры.
- `test_add_book_in_favorites_adds_existing_only_and_without_duplicates` — добавление в избранное только существующих книг и запрет дублей.
- `test_delete_book_from_favorites_removes_if_present` — удаление из избранного, отсутствие эффекта при удалении отсутствующей книги.
- `test_get_list_of_favorites_books_returns_favorites_list` — возврат списка избранных книг.

Запуск:
`pytest -v tests.py`