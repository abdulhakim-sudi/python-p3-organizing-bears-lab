def test_create_bears_table_exists(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bears';")
    table = cursor.fetchone()
    assert table is not None

def test_bears_table_has_correct_columns(cursor):
    cursor.execute("PRAGMA table_info(bears);")
    columns = [column[1] for column in cursor.fetchall()]
    expected_columns = ['id', 'name', 'age', 'sex', 'color', 'temperament', 'alive']
    for col in expected_columns:
        assert col in columns
