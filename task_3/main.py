import sys
from log_parser import load_logs, filter_logs_by_level, count_logs_by_level
from log_display import display_level_logs, display_log_counts

def main():
    if len(sys.argv) > 1:
        _, path, *args = sys.argv
        parsed_logs = load_logs(path) # Завантажуємо логи з файлу
        counted_levels = count_logs_by_level(parsed_logs) # Рахуємо кількість логів за рівнем
        display_log_counts(counted_levels) # Відображаємо кількість логів за рівнем
        if len(args):
            level = args[0].upper()
            filtered_logs = filter_logs_by_level(parsed_logs, level)  #Фільтруємо логи за рівнем
            display_level_logs(filtered_logs, level) # Відображаємо логи відфільтровані за рівнем
            
if __name__ == "__main__":
    main()
    