def log_test(func):
    def wrapper(*args, **kwargs):
        print("Запуск тесту")
        result = func(*args, **kwargs)
        print("Тест завершено")
        return result
    return wrapper


def log_function(func):
    """Декоратор, який логує аргументи та результат функції."""
    def wrapper(*args, **kwargs):
        print(f"Викликаємо '{func.__name__}' з аргументами: args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"Функція '{func.__name__}' повернула: {result}")
        return result
    return wrapper


def catch_exceptions(func):
    """Декоратор, який перехоплює та обробляє винятки."""
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Помилка в функції '{func.__name__}': {e}")
            return None
    return wrapper


if __name__ == "__main__":
    @log_function
    def add(a, b):
        return a + b

    @catch_exceptions
    def divide(a, b):
        return a / b

    print("=== Тест log_function ===")
    add(5, 3)

    print("\n=== Тест catch_exceptions ===")
    divide(10, 0)