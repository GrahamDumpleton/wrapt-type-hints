from decorators.pass_through import pass_through


@pass_through
def function(a: int, b: int) -> int:
    return a + b

result: int = function(2, "three") # type: ignore[arg-type]
