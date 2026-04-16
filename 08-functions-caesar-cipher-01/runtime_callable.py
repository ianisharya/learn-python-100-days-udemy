"""
Utility module for cross-cutting concerns.

Provides decorators that can be applied across functions
"""

import functools
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")

def runtime_only(func: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator to add runtime behaviour.

    Args:
        func: Function to wrap

    Returns:
        Wrapped function with additional runtime behaviour
    """
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f'Runtime call: "{func.__name__}"')
        return func(*args, **kwargs)

    return wrapper

# end of file