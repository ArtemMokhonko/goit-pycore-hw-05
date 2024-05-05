def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            if func.__name__ == 'show_phone':
                return "Give me name"
            else:
                return "Give me name and phone please"
        except KeyError:
            return "Contact not found."
        except Exception as error:
            return f"An unexpected error occurred: {error}"
    return inner