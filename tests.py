import pytest
from main import BooksCollector


class TestBooksCollector:

    @pytest.fixture
    def collector(self):
        return BooksCollector()

    def test_add_new_book_success(self, collector):
        collector.add_new_book('Book_1')
        assert 'Book_1' in collector.books_genre

    def test_add_new_book_empty_name(self, collector):
        collector.add_new_book('')
        assert '' not in collector.books_genre

    def test_set_books_genre_success(self, collector):
        collector.add_new_book('Book_1')
        collector.set_book_genre('Book_1', 'Комедии')
        assert collector.books_genre['Book_1'] == 'Комедии'

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Book_2')
        collector.set_book_genre('Book_2', 'Поэма')
        assert collector.books_genre['Book_2'] == ''

    def test_get_book_genre_existing_book(self, collector):
        collector.add_new_book('Book_3')
        collector.set_book_genre('Book_3', 'Мультфильмы')
        assert collector.get_book_genre('Book_3') == 'Мультфильмы'

    @pytest.mark.parametrize('book, genre', [['Book_4', 'Детективы'], ['Book_5', 'Детективы']])
    def test_get_books_with_specific_genre_success(self, collector, book, genre):
        collector.add_new_book(book)
        collector.set_book_genre(book, genre)
        books = collector.get_books_with_specific_genre(genre)
        assert book in books

    def test_get_books_with_specific_genre_non_existing_genre(self, collector):
        collector.add_new_book('Book_6')
        collector.set_book_genre('Book_6', 'Фантастика')
        books = collector.get_books_with_specific_genre('Ужасы')
        assert books == []

    def test_get_books_genre_success(self, collector):
        assert collector.get_books_genre() == {}

    def test_get_books_for_children_success(self, collector):
        collector.add_new_book('Book_7')
        collector.set_book_genre('Book_7', 'Мультфильмы')
        children = collector.get_books_for_children()
        assert 'Book_7' in children

    def test_add_book_in_favorites_success(self, collector):
        collector.add_new_book('Book_8')
        collector.add_book_in_favorites('Book_8')
        assert 'Book_8' in collector.favorites

    def test_delete_book_from_favorites_success(self, collector):
        collector.add_new_book('Book_9')
        collector.add_book_in_favorites('Book_9')
        collector.delete_book_from_favorites('Book_9')
        assert 'Book_9' not in collector.favorites

    @pytest.mark.parametrize('name', ['Book_10', 'Book_11'])
    def test_get_list_of_favorites_books_success(self, collector, name):
        collector.add_new_book(name)
        collector.add_book_in_favorites(name)
        favorites_list = collector.get_list_of_favorites_books()
        assert name in favorites_list
