from decorators.pass_through_decorator import pass_through_decorator


@pass_through_decorator
def function(a: int, b: int) -> int:
    return a + b


result: str = function(2, 3)
