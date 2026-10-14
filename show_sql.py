import duckdb
import matplotlib.pyplot as plt

# Считаем пользователей по устройству и долю от общего числа пользователей.
df = duckdb.sql("""
    SELECT
        device,
        COUNT(*) AS total,
        COUNT(*) * 100.0 / SUM(COUNT(*)) OVER () AS percent
    FROM 'users.csv'
    GROUP BY device
    ORDER BY total DESC
""").df()

print(df.to_string(index=False, formatters={"percent": "{:.1f}%".format}))

# Высота столбца — точное число пользователей; подпись — число и процент.
fig, ax = plt.subplots()
bars = ax.bar(df["device"], df["total"])
ax.bar_label(
    bars,
    labels=[f"{count} ({percent:.1f}%)" for count, percent in zip(df["total"], df["percent"])],
    padding=3,
)

ax.set_xlabel("Device")
ax.set_ylabel("Users")
ax.set_title("Users by Device")
ax.margins(y=0.15)  # Место над столбцами для подписей.
fig.tight_layout()
plt.show()
