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
    connection = lite.connect(database_path)
    with connection:  # With is a substitute for the try/finally flow for assuring d/c after execution
        cursor = connection.cursor()
        for word in word_list:
            # check to see if word is present. If present increment, else add
            sql = "select count(word) from words WHERE word='" + word + "'"
            cursor.execute(sql)
            count = cursor.fetchone()[0]
            if count > 0:
                sql = "update words set usage_count=usage_count+1 where word='" + word + "'"
            else:
                sql = "insert into words(word) values ('" + word + "') "  # Inserting the current word into the words table, word col
            cursor.execute(sql)
    print("Changes made to DB")