def caching_fibonacci():
    cache = {} # Порожній словник для кешу
    
    def fibonacci(n:str):
        if n <= 0: 
            return 0
        elif n == 1:
            return 1
        elif n in cache:     # Якщо n у cache вертаемо значення з кешу        
            return cache[n] 

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2) # Використовуємо рекурсію для обчислення числа n-те
        return cache[n]
    return fibonacci 
    

fib = caching_fibonacci()
# Використовуємо функцію fibonacci для обчислення чисел Фібоначчі
print(fib(10))  
print(fib(15))


