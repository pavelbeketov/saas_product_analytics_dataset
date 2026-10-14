import duckdb
import numpy

result = duckdb.sql("""
    SELECT *
    FROM events.csv;
""")

print(result.df())