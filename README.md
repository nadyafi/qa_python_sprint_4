# qa_python
Для методов add_new_book, set_book_genre, get_books_with_specific_genre реализованы позитивные и негативные сценарии проверки.
Для методов get_book_genre, get_books_genre, get_books_for_children, add_book_in_favorites, delete_book_from_favorites, get_list_of_favorites_books реализованы позитивные тесты.
tests.py::TestBooksCollector::test_add_new_book_success PASSED                                                                                            [  7%]
tests.py::TestBooksCollector::test_add_new_book_empty_name PASSED                                                                                         [ 14%]
tests.py::TestBooksCollector::test_set_books_genre_success PASSED                                                                                         [ 21%]
tests.py::TestBooksCollector::test_set_book_genre_invalid_genre PASSED                                                                                    [ 28%]
tests.py::TestBooksCollector::test_get_book_genre_existing_book PASSED                                                                                    [ 35%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_success[Book_4-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED            [ 42%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_success[Book_5-\u0414\u0435\u0442\u0435\u043a\u0442\u0438\u0432\u044b] PASSED            [ 50%]
tests.py::TestBooksCollector::test_get_books_with_specific_genre_non_existing_genre PASSED                                                                [ 57%]
tests.py::TestBooksCollector::test_get_books_genre_success PASSED                                                                                         [ 64%]
tests.py::TestBooksCollector::test_get_books_for_children_success PASSED                                                                                  [ 71%]
tests.py::TestBooksCollector::test_add_book_in_favorites_success PASSED                                                                                   [ 78%]
tests.py::TestBooksCollector::test_delete_book_from_favorites_success PASSED                                                                              [ 85%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_success[Book_10] PASSED                                                                    [ 92%]
tests.py::TestBooksCollector::test_get_list_of_favorites_books_success[Book_11] PASSED                                                                    [100%]

====================================================================== 14 passed in 0.01s =======================================================================