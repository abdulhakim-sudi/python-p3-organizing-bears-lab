import pytest
import sqlite3

@pytest.fixture
def cursor():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    with open("lib/create.sql") as create_file:
        cursor.executescript(create_file.read())

    try:
        with open("lib/insert.sql") as insert_file:
            cursor.executescript(insert_file.read())
    except:
        pass

    yield cursor

    connection.close()
