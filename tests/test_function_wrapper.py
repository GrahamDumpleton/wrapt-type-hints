from decorators.pass_through_wrapper import pass_through_wrapper


@pass_through_wrapper
def function(a: int, b: int) -> int:
    return a + b


result: int = function(2, 3)
