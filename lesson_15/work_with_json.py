# Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
# результат для невалідного файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log

from pathlib import Path
import json
import logging

# Папка с json файлами
json_folder = Path(__file__).parent / "work_with_json"

# путь к лог файлу
result_file = Path(__file__).parent / "json__terzeman.log"

# н7астройки логера
logging.basicConfig(
    filename=result_file,
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

for json_file in json_folder.iterdir():
    if json_file.suffix == ".json":
        try:
            with open(json_file, encoding="utf-8") as f:
                data = json.load(f)
            print(f"{json_file.name}: valid")
        except json.JSONDecodeError as e:
            print(f"{json_file.name}: invalid — {e}")
            logging.error(f"{json_file.name}: invalid JSON — {e}")