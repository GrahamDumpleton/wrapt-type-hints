from typing import Any, Callable, ParamSpec, TypeVar

from versions import wrapt

P = ParamSpec("P")
R = TypeVar("R")


@wrapt.decorator
def pass_through(
    wrapped: Callable[P, R],
    instance: Any,
    args: tuple[Any, ...],
    kwargs: dict[str, Any],
) -> R:
    return wrapped(*args, **kwargs)
