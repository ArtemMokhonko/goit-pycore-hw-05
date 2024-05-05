import re
from typing import Callable


def generator_numbers(text: str):
    pattern = r"\d+\.\d+"       # Регулярний вираз для пошуку дійсних чисел
    for matches in re.findall(pattern, text):
        yield float(matches)    # Повертає числа як генератор   

def sum_profit(text: str, func: Callable) -> float:
    return sum(func(text))  # Розраховує загальний дохід
    

text = "Загальний дохід працівника складається\
з декількох частин: 1000.01 як основний дохід,\
доповнений додатковими надходженнями 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


