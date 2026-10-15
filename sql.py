import duckdb
import numpy

result = duckdb.sql("""
SELECT device
FROM users.csv
group by device;

""")

print(result.df())