# Візміть два файли з теки ideas_for_test/work_with_csv,
# порівняйте на наявність дублікатів і приберіть їх.
# Результат запишіть у файл result_<your_second_name>.csv

from pathlib import Path
import csv

# Папка с CSV файлами
csv_folder = Path(__file__).parent / "work_with_csv"

# Читаем файл 1
file_1 = csv_folder / "r-m-c.csv"
rows_1 = []

with open(file_1, encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        rows_1.append(row)

# Читаем файл 2 делаем список
file_2 = csv_folder / "random-michaels.csv"
rows_2 = []

with open(file_2, encoding="utf-8") as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        rows_2.append(row)

# Создаём файл, убираем дубликаты
csv_folder = Path(__file__).parent / "work_with_csv"

result_file = csv_folder / "Terzeman.csv"

result = []
for row in rows_1 + rows_2:
    if row not in result:
        result.append(row)

with open(result_file, "w", encoding="utf-8", newline = "") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerows(result)



