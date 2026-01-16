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

result_im: int = instance.function_im(2, "three")

result_cm_1: int = Test.function_cm(2, "three")
result_cm_2: int = instance.function_cm(2, "three")

result_sm_1: int = Test.function_sm(2, "three")
result_sm_2: int = instance.function_sm(2, "three")
