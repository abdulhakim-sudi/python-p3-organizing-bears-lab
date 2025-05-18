def test_correct_number_of_bears_inserted(cursor):
    cursor.execute("SELECT COUNT(*) FROM bears;")
    count = cursor.fetchone()[0]
    assert count == 8
