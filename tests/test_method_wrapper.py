from decorators.pass_through_wrapper import pass_through_wrapper


class Test:
    @pass_through_wrapper
    def function_im(self, a: int, b: int) -> int:
        return a + b

    @pass_through_wrapper
    @classmethod
    def function_cm(cls, a: int, b: int) -> int:
        return a + b

    @pass_through_wrapper
    @staticmethod
    def function_sm(a: int, b: int) -> int:
        return a + b


instance = Test()

result_im: int = instance.function_im(2, 3)

result_cm_1: int = Test.function_cm(2, 3)
result_cm_2: int = instance.function_cm(2, 3)

result_sm_1: int = Test.function_sm(2, 3)
result_sm_2: int = instance.function_sm(2, 3)
