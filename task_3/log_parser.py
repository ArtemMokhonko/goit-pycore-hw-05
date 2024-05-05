import re
from collections import Counter

# Функція для розбору рядків логів
def parse_log_line(line: str) -> dict: 
    try:
        pattern = r'(\d{4}-\d{2}-\d{2}) (\d{2}:\d{2}:\d{2}) (\w+) (.*)'
        match = re.match(pattern, line)
        if match:
            date, time, level, message = match.groups()
            return {
                "date": date,
                "time": time,
                "level": level.upper(),
                "message": message,
            }
    except ValueError:
        print("Wrong log format:", line)
        return None

# Функція для завантаження логів з файлу
def load_logs(path): 
    try:
        with open(path, 'r', encoding='utf-8') as file:
            records = [rec.strip() for rec in file.readlines() if rec.strip()]
        logs = [parse_log_line(rec) for rec in records]
        logs_filtered = [rec for rec in logs if rec]
        return logs_filtered
    except FileNotFoundError:
        print('File not found')
        return []
    except Exception as error:
        print('Error reading logs:', error)
        return []

# Функція для фільтрації логів за рівнем
def filter_logs_by_level(logs: list[dict], level: str) -> list[dict]:
    return filter(lambda x: x['level'] == level.upper(), logs)
    

# Функція для підрахунку логів за рівнем
def count_logs_by_level(logs: list[dict]) -> dict: 
    level_list = [log['level'] for log in logs ]
    return Counter(level_list)
