from decorators.pass_through import pass_through


class Test:
    @pass_through
    def function_im(self, a: int, b: int) -> int:
        return a + b

    @pass_through
    @classmethod
    def function_cm(cls, a: int, b: int) -> int:
        return a + b

    @pass_through
    @staticmethod
    def function_sm(a: int, b: int) -> int:
        return a + b


instance = Test()

result_im: str = instance.function_im(2, 3)

result_cm_1: str = Test.function_cm(2, 3)
result_cm_2: str = instance.function_cm(2, 3)

result_sm_1: str = Test.function_sm(2, 3)
result_sm_2: str = instance.function_sm(2, 3)
