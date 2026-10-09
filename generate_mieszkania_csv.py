import csv
from pathlib import Path

output_path = Path("mieszkania_1000.csv")
header = ["Metraz", "Pokoje", "Centrum", "Zly_Stan", "Cena"]
rows = []

for i in range(1, 1001):
    metraz = 25 + ((i * 11) % 90) + (12 if i % 7 == 0 else 0)
    pokoje = 1 + ((i * 3) % 5)
    centrum = 1 if i % 4 == 0 else 0
    zly_stan = 1 if i % 5 == 0 else 0
    cena = int(
        metraz * (11000 + pokoje * 700 + centrum * 1800 - zly_stan * 2200)
        + (i * 137) % 90000
    )
    rows.append([metraz, pokoje, centrum, zly_stan, cena])

with output_path.open("w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print(f"Utworzono {len(rows)} rekordów w {output_path}")
