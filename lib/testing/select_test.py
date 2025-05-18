from lib.sql_queries import (
    select_all_female_bears_return_name_and_age,
)

def test_select_all_female_bears_return_name_and_age(cursor):
    cursor.execute(select_all_female_bears_return_name_and_age)
    results = cursor.fetchall()
    assert len(results) > 0
    for result in results:
        assert isinstance(result[0], str)  # name
        assert isinstance(result[1], int)  # age
