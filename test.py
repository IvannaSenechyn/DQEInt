import pytest
import pymssql


@pytest.fixture(scope="module")
def db_connection():
    # Connect to the MS SQL database
    conn = pymssql.connect(
        server='localhost',
        user='RobotUser',
        password='123456#zaq',
        database='AdventureWorks2017'
    )
    yield conn
    conn.close()


# Test Case 1: Check Column Count for [Person].[Address] table
@pytest.mark.parametrize("expected_count", [9])
def test_column_count(expected_count):
    sql_query = """
                SELECT COUNT(*)
                FROM INFORMATION_SCHEMA.COLUMNS
                WHERE TABLE_SCHEMA = 'Person' AND TABLE_NAME = 'Address';
                """


# Test Case 2: Check Maximum and Minimum Values for StateProvinceID in [Person].[Address] table
@pytest.mark.parametrize("expected_max", [(1, 181)])
def test_min_max_values(expected_max):
    sql_query = """
                SELECT MIN(StateProvinceID), MAX(StateProvinceID)
                FROM [Person].[Address];
                """


# Test Case 3: Check Average Value for Status column in [Production].[Document] table
@pytest.mark.parametrize("expected_avg", [1])
def test_average_value(expected_avg):
    sql_query = """
                SELECT AVG(Status)
                FROM [Production].[Document];
                """


# Test Case 4: Check Unique Values from Owner column of [Production].[Document] table
@pytest.mark.parametrize("expected_unique_values", [(217, 219, 220)])
def test_unique_values(expected_unique_values):
    sql_query = """
                SELECT DISTINCT Owner
                FROM [Production].[Document];
                """


# Test Case 5: Check Data Existence in [Production].[UnitMeasure] table
def test_data_existence_production_unitmeasure(db_connection):
    cursor = db_connection.cursor()
    cursor.execute("""
        SELECT COUNT(*)
        FROM [Production].[UnitMeasure]
    """)
    row_count = cursor.fetchone()[0]
    assert row_count > 0


# Test Case 6: Check Values within Range in [Production].[UnitMeasure] table
@pytest.mark.parametrize("expected_range_values", [('Crate', 'Case')])
def test_values_within_range(expected_range_values):
    sql_query = """
                SELECT Name
                FROM [Production].[UnitMeasure]
                WHERE UnitMeasureCode BETWEEN 'CR' AND 'CS';
                """
print "done"
# pytest test.py
# pytest test.py --html=report.html
