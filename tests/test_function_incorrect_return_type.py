from decorators.pass_through import pass_through


@pass_through
def function(a: int, b: int) -> int:
    return a + b

result: str = function(2, 3) # type: ignore[return-value,assignment]
