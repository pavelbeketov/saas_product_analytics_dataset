import duckdb
import numpy

result = duckdb.sql("""
SELECT * 
FROM payments.csv;
""")

print(result.df())