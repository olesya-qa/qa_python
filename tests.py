from main import BooksCollector
import pytest


class TestBooksCollector:
    def test_add_new_book_adds_books_and_sets_empty_genre(self):
        collector = BooksCollector()

        name_1 = "Book_1"
        name_2 = "Book_2"
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)

        books = collector.get_books_genre()
        assert len(books) == 2
        assert books[name_1] == ""
        assert books[name_2] == ""

    @pytest.mark.parametrize(
        "initial,to_add,expected_keys",
        [
            ([], ["short"], ["short"]),  # валидное добавление
            ([], [""], []),  # пустое название
            ([], ["a" * 41], []),  # длина больше 40
            (["Valid"], ["Valid"], ["Valid"]),  # повторное добавление
            (["Valid"], ["Valid", "Valid"], ["Valid"]),  # многократные повторы
        ],
    )
    def test_add_new_book_rejects_invalid_names_and_duplicates(
        self, initial, to_add, expected_keys
    ):
        collector = BooksCollector()

        for book_name in initial:
            collector.add_new_book(book_name)
        for book_name in to_add:
            collector.add_new_book(book_name)

        books = collector.get_books_genre()
        assert set(books.keys()) == set(expected_keys)
        for key in expected_keys:
            assert books[key] == ""

    @pytest.mark.parametrize(
        "existing_name,genre,expected_books_genre",
        [
            ("Book", "Фантастика", {"Book": "Фантастика"}),  # валидный жанр
            ("Book", "Неизвестный_жанр", {"Book": ""}),  # не валидный жанр
            (None, "Фантастика", {}),  # книги нет в books_genre
        ],
    )
    def test_set_book_genre_sets_only_for_existing_books_and_valid_genres(
        self, existing_name, genre, expected_books_genre
    ):
        collector = BooksCollector()

        if existing_name is not None:
            collector.add_new_book(existing_name)
            collector.set_book_genre(existing_name, genre)
        else:
            collector.set_book_genre("Book", genre)

        assert collector.get_books_genre() == expected_books_genre

    @pytest.mark.parametrize(
        "name,expected",
        [
            ("Known", "Комедии"),
            ("Unknown", None),
        ],
    )
    def test_get_book_genre_returns_genre_or_none(self, name, expected):
        collector = BooksCollector()
        collector.add_new_book("Known")
        collector.set_book_genre("Known", "Комедии")

        assert collector.get_book_genre(name) == expected

    @pytest.mark.parametrize(
        "genre,expected",
        [
            ("Фантастика", ["A", "C"]),
            ("Ужасы", ["B"]),
            ("Неверный_жанр", []),
        ],
    )
    def test_get_books_with_specific_genre_filters_correctly(
        self, genre, expected
    ):
        collector = BooksCollector()
        collector.add_new_book("A")
        collector.add_new_book("B")
        collector.add_new_book("C")

        collector.set_book_genre("A", "Фантастика")
        collector.set_book_genre("B", "Ужасы")
        collector.set_book_genre("C", "Фантастика")

        assert collector.get_books_with_specific_genre(genre) == expected

    def test_get_books_genre_returns_current_dict(self):
        collector = BooksCollector()

        collector.add_new_book("A")
        collector.add_new_book("B")
        collector.set_book_genre("A", "Детективы")
        collector.set_book_genre("B", "Мультфильмы")

        assert collector.get_books_genre() == {"A": "Детективы", "B": "Мультфильмы"}

    def test_get_books_for_children_excludes_age_rated_genres(self):
        collector = BooksCollector()

        collector.add_new_book("Child_OK")
        collector.add_new_book("No_1_Uzhasy")
        collector.add_new_book("No_2_Detectives")
        collector.add_new_book("No_3_Unassigned")

        collector.set_book_genre("Child_OK", "Комедии")
        collector.set_book_genre("No_1_Uzhasy", "Ужасы")
        collector.set_book_genre("No_2_Detectives", "Детективы")
        # "No_3_Unassigned" остаётся с пустым жанром ""

        assert collector.get_books_for_children() == ["Child_OK"]

    @pytest.mark.parametrize(
        "existing,add_times,expected_favorites",
        [
            (True, 1, ["Book"]),  # успешное добавление
            (True, 2, ["Book"]),  # не добавляется повторно
            (False, 1, []),  # нельзя добавить книгу, которой нет в словаре
        ],
    )
    def test_add_book_in_favorites_adds_existing_only_and_without_duplicates(
        self, existing, add_times, expected_favorites
    ):
        collector = BooksCollector()

        if existing:
            collector.add_new_book("Book")

        for _ in range(add_times):
            collector.add_book_in_favorites("Book")

        assert collector.favorites == expected_favorites

    @pytest.mark.parametrize(
        "initial_favorites,delete_name,expected_favorites",
        [
            (["Book"], "Book", []),
            (["Book"], "Unknown", ["Book"]),
            ([], "Book", []),
        ],
    )
    def test_delete_book_from_favorites_removes_if_present(
        self, initial_favorites, delete_name, expected_favorites
    ):
        collector = BooksCollector()
        collector.favorites = list(initial_favorites)

        collector.delete_book_from_favorites(delete_name)

        assert collector.favorites == expected_favorites

    def test_get_list_of_favorites_books_returns_favorites_list(self):
        collector = BooksCollector()
        collector.add_new_book("A")
        collector.add_new_book("B")

        collector.add_book_in_favorites("A")
        collector.add_book_in_favorites("B")

        assert collector.get_list_of_favorites_books() == ["A", "B"]