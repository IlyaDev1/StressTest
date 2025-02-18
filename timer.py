from datetime import datetime, timedelta


def wrapper(func):
    def inner(*args, **kwargs) -> timedelta:
        start = datetime.now()
        func(*args, **kwargs)
        elapsed = datetime.now() - start
        return elapsed

    return inner
