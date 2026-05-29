import pytest


class TestBooksCollector:

    def test_add_new_book_adds_books_and_sets_empty_genre(self, collector):
        name_1 = "Book_1"
        name_2 = "Book_2"
        collector.add_new_book(name_1)
        collector.add_new_book(name_2)

        books = collector.get_books_genre()
        assert len(books) == 2
        assert books[name_1] == ""
        assert books[name_2] == ""

    @pytest.mark.parametrize("name", ["a", "a" * 40])
    def test_add_new_book_valid_boundary_name_lengths(self, collector, name):
        collector.add_new_book(name)

        books = collector.get_books_genre()
        assert name in books
        assert books[name] == ""

    @pytest.mark.parametrize("name", ["", "a" * 41])
    def test_add_new_book_invalid_name_lengths_not_added(self, collector, name):
        collector.add_new_book(name)

        assert collector.get_books_genre() == {}

    def test_add_new_book_duplicate_not_added_twice(self, collector):
        collector.add_new_book("Valid")
        collector.add_new_book("Valid")

        books = collector.get_books_genre()
        assert list(books.keys()) == ["Valid"]
        assert books["Valid"] == ""

    @pytest.mark.parametrize(
        "genre",
        ["Фантастика", "Ужасы", "Детективы", "Мультфильмы", "Комедии"],
    )
    def test_set_book_genre_sets_valid_genre(self, collector, genre):
        collector.add_new_book("Book")
        collector.set_book_genre("Book", genre)

        assert collector.get_book_genre("Book") == genre

    def test_set_book_genre_invalid_genre_not_set(self, collector):
        collector.add_new_book("Book")
        collector.set_book_genre("Book", "Неизвестный_жанр")

        assert collector.get_book_genre("Book") == ""

    def test_set_book_genre_for_nonexistent_book_does_nothing(self, collector):
        collector.set_book_genre("Book", "Фантастика")

        assert collector.get_books_genre() == {}

    def test_get_book_genre_returns_set_genre(self, collector):
        collector.add_new_book("Known")
        collector.set_book_genre("Known", "Комедии")

        assert collector.get_book_genre("Known") == "Комедии"

    def test_get_book_genre_returns_none_for_unknown_book(self, collector):
        assert collector.get_book_genre("Unknown") is None

    @pytest.mark.parametrize(
        "genre",
        ["Фантастика", "Ужасы", "Комедии"],
    )
    def test_get_books_with_specific_genre_returns_matching_books(
        self, collector, genre
    ):
        collector.add_new_book("Book")
        collector.set_book_genre("Book", genre)

        assert collector.get_books_with_specific_genre(genre) == ["Book"]

    def test_get_books_with_specific_genre_returns_empty_for_unknown_genre(
        self, collector
    ):
        collector.add_new_book("Book")
        collector.set_book_genre("Book", "Фантастика")

        assert collector.get_books_with_specific_genre("Неверный_жанр") == []

    def test_get_books_genre_returns_current_dict(self, collector):
        collector.add_new_book("A")
        collector.add_new_book("B")
        collector.set_book_genre("A", "Детективы")
        collector.set_book_genre("B", "Мультфильмы")

        assert collector.get_books_genre() == {"A": "Детективы", "B": "Мультфильмы"}

    def test_get_books_for_children_excludes_age_rated_genres(self, collector):
        collector.add_new_book("Child_OK")
        collector.add_new_book("No_1_Uzhasy")
        collector.add_new_book("No_2_Detectives")
        collector.add_new_book("No_3_Unassigned")

        collector.set_book_genre("Child_OK", "Комедии")
        collector.set_book_genre("No_1_Uzhasy", "Ужасы")
        collector.set_book_genre("No_2_Detectives", "Детективы")

        assert collector.get_books_for_children() == ["Child_OK"]

    def test_add_book_in_favorites_adds_existing_book(self, collector):
        collector.add_new_book("Book")
        collector.add_book_in_favorites("Book")

        assert collector.get_list_of_favorites_books() == ["Book"]

    def test_add_book_in_favorites_not_added_twice(self, collector):
        collector.add_new_book("Book")
        collector.add_book_in_favorites("Book")
        collector.add_book_in_favorites("Book")

        assert collector.get_list_of_favorites_books() == ["Book"]

    def test_add_book_in_favorites_nonexistent_book_not_added(self, collector):
        collector.add_book_in_favorites("Book")

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_removes_book(self, collector):
        collector.favorites = ["Book"]
        collector.delete_book_from_favorites("Book")

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_unknown_book_not_removed(self, collector):
        collector.favorites = ["Book"]
        collector.delete_book_from_favorites("Unknown")

        assert collector.get_list_of_favorites_books() == ["Book"]

    def test_delete_book_from_favorites_empty_list_unchanged(self, collector):
        collector.delete_book_from_favorites("Book")

        assert collector.get_list_of_favorites_books() == []

    def test_get_list_of_favorites_books_returns_favorites_list(self, collector):
        collector.add_new_book("A")
        collector.add_new_book("B")
        collector.add_book_in_favorites("A")
        collector.add_book_in_favorites("B")

        assert collector.get_list_of_favorites_books() == ["A", "B"]
