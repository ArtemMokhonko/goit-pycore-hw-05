# Функція для відображення кількості логів за рівнем
def display_log_counts(counts: dict):
    print('Рівень логування | Кількість')
    print('-----------------|----------')
    for level, count in counts.items():
        print(f'{level:<17}|{count:<10}')
        
    
# Функція для відображення логів відфільтрованих за рівнем    
def display_level_logs(level_logs: list[dict], level: str):
    print(f"Деталі логів для рівня '{level}'")
    for log in level_logs:
        print(f"{log['date']} {log['time']} - {log['message']}")