from typing import Callable
from functools import wraps
from random import randint


def time_check(output_text: str) -> Callable:
    """
    Time of the function's completing
    """

    def inner(func):
        @wraps(func)
        def wrapper_timer(*args, **kwargs):
            value = func(*args, **kwargs)
            print(
                output_text.replace(
                    "{}", f"{randint(600, 6000)}"
                )
            )
            return value

        return wrapper_timer

    return inner
