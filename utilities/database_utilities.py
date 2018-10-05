import sqlite3 as lite


def create_database(database_path: str):
    connection = lite.connect(database_path)
    with connection:
        cursor = connection.cursor()
        cursor.execute("drop table if exists words")
        ddl = "CREATE TABLE words  ( word TEXT NOT NULL PRIMARY KEY, usage_count INT DEFAULT 1 NOT NULL  ); "
        cursor.execute(ddl)
        ddl = "CREATE UNIQUE INDEX words_word_uindex ON words (word);"
        cursor.execute(ddl)


def save_words_to_database(database_path: str, word_list: list):
    # TODO: save words to db
    pass
