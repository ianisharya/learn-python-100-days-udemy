"""
Utility module for cross-cutting concerns.

Provides decorators that can be applied across functions
(e.g., logging, tracing, monitoring).
"""

import functools
from typing import Callable, TypeVar, ParamSpec

P = ParamSpec("P")
R = TypeVar("R")


def runtime_only(func: Callable[P, R]) -> Callable[P, R]:
    """
    Decorator to add runtime behavior (e.g., logging/tracing)
    without modifying core business logic.

    Args:
        func: Function to wrap

    Returns:
        Wrapped function with additional runtime behavior
    """
    @functools.wraps(func)
    def wrapper(*args: P.args, **kwargs: P.kwargs) -> R:
        print(f'Runtime logic here for function "{func.__name__}"')
        return func(*args, **kwargs)

    return wrapper