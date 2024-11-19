import json
import csv

class DataSaver:
    """Клас для збереження даних у різні формати"""

    def save_data(self, data, file_format="json"):
        """Збереження даних у обраному форматі"""
        filename = f"data.{file_format}"
        try:
            if file_format == "json":
                with open(filename, "w") as f:
                    json.dump(data, f, indent=4)
            elif file_format == "csv":
                with open(filename, "w", newline='') as f:
                    writer = csv.writer(f)
                    writer.writerow(data[0].keys())
                    for row in data:
                        writer.writerow(row.values())
            elif file_format == "txt":
                with open(filename, "w") as f:
                    f.write(str(data))
            print(f"Дані збережено у файл {filename}.")
        except Exception as e:
            print(f"Помилка при збереженні даних: {e}")
