from inspect import FullArgSpec
from typing import Any, Callable, Concatenate, ParamSpec, TypeVar, overload

from wrapt import (
    AdapterFactory,
    Boolean,
    ClassMethodWrapperFunction,
    Descriptor,
    GenericCallableWrapperFunction,
    InstanceMethodWrapperFunction,
    ObjectProxy,
    P,
    R,
    T,
    WrappedFunction,
    WrapperFunction,
)

P1 = ParamSpec("P1")
R1 = TypeVar("R1", covariant=True)

T1 = TypeVar("T1", bound=Any)

P2 = ParamSpec("P2")
R2 = TypeVar("R2", covariant=True)

T2 = TypeVar("T2", bound=Any)

class _FunctionWrapperBase(ObjectProxy[WrappedFunction[P, R]]):
    _self_instance: Any
    _self_wrapper: WrapperFunction[P, R]
    _self_enabled: bool | Boolean | Callable[[], bool] | None
    _self_binding: str
    _self_parent: Any
    _self_owner: Any

class V2_BoundFunctionWrapper(_FunctionWrapperBase[P1, R1]):
    def __call__(self, *args: P1.args, **kwargs: P1.kwargs) -> R1: ...

    # Note that for following overloads, testing with mypy and ty they still do
    # not handle static methods being decorated but to best knowledge this is
    # a limitation in those type checkers. Testing with pyrefly fails on any
    # type of bound method. Testing with pyright handles case correctly.
    #
    # Also, note that use of T2, P2 and R2 in first two cases is also required
    # to ensure correct handling by mypy and ty, so do not change to use of T1,
    # P1 and R1.

    @overload
    def __get__(  # Required to ensure mypy, pyrefly and ty works correctly
        self: V2_BoundFunctionWrapper[Concatenate[T2, P2], R2],
        instance: T2,
        owner: type[T2] | None = None,
    ) -> V2_BoundFunctionWrapper[P2, R2]: ...
    @overload
    def __get__(  # Required to ensure mypy, pyrefly and ty works correctly
        self: V2_BoundFunctionWrapper[Concatenate[T2, P2], R2],
        instance: T,
        owner: type[Any] | None = None,
    ) -> V2_BoundFunctionWrapper[P2, R2]: ...
    @overload
    def __get__(  # Required to ensure mypy, pyrefly and ty works correctly
        self, instance: None, owner: type[T1] | None = None
    ) -> V2_BoundFunctionWrapper[P1, R1]: ...
    @overload
    def __get__(  # Required to ensure pyright works correctly
        self, instance: T1, owner: type[T1] | None = None
    ) -> V2_BoundFunctionWrapper[P1, R1]: ...

class V2_FunctionWrapper(_FunctionWrapperBase[P1, R1]):
    def __init__(
        self,
        wrapped: WrappedFunction[P1, R1],
        wrapper: WrapperFunction[P1, R1],
        enabled: bool | Boolean | Callable[[], bool] | None = None,
    ) -> None: ...
    def __call__(self, *args: P1.args, **kwargs: P1.kwargs) -> R1: ...

    # Note that for following overloads, testing with mypy and ty they still do
    # not handle static methods being decorated but to best knowledge this is
    # a limitation in those type checkers. Testing with pyrefly fails on any
    # type of bound method. Testing with pyright handles case correctly.
    #
    # Also, note that use of T2, P2 and R2 in first two cases is also required
    # to ensure correct handling by mypy and ty, so do not change to use of T1,
    # P1 and R1.

    @overload
    def __get__(  # Required to ensure mypy, pyrefly and ty works correctly
        self: V2_FunctionWrapper[Concatenate[T2, P2], R2],
        instance: T2,
        owner: type[Any] | None = None,
    ) -> V2_BoundFunctionWrapper[P2, R2]: ...
    @overload
    def __get__(  # Required to ensure mypy, pyrefly and ty works correctly
        self: V2_FunctionWrapper[Concatenate[T2, P2], R2],
        instance: T2,
        owner: type[T2] | None = None,
    ) -> V2_BoundFunctionWrapper[P2, R2]: ...
    @overload
    def __get__(  # Required to ensure mypy, pyrefly and ty works correctly
        self, instance: None, owner: type[T1] | None = None
    ) -> V2_BoundFunctionWrapper[P1, R1]: ...
    @overload
    def __get__(  # Required to ensure pyright works correctly
        self, instance: T1, owner: type[T1] | None = None
    ) -> V2_BoundFunctionWrapper[P1, R1]: ...

class V2_FunctionDecorator:
    @overload
    def __call__(
        self,
        callable: (
            Callable[P, R]
            | Callable[Concatenate[type[T], P], R]
            # | Callable[Concatenate[Any, P], R]  # Breaks mypy, pyrefly and ty
            | Callable[[type[T]], R]
        ),
    ) -> V2_FunctionWrapper[P, R]: ...
    @overload
    def __call__(self, callable: Descriptor) -> V2_FunctionWrapper[P, Any]: ...

class V2_PartialFunctionDecorator:
    @overload
    def __call__(
        self, wrapper: GenericCallableWrapperFunction[P, R], /
    ) -> V2_FunctionDecorator: ...
    @overload
    def __call__(
        self, wrapper: ClassMethodWrapperFunction[P, R], /
    ) -> V2_FunctionDecorator: ...
    @overload
    def __call__(
        self, wrapper: InstanceMethodWrapperFunction[P, R], /
    ) -> V2_FunctionDecorator: ...

@overload
def decorator(wrapper: type[T], /) -> V2_FunctionDecorator: ...

# ... Decorator applied to function or method.

@overload
def decorator(
    wrapper: GenericCallableWrapperFunction[P, R], /
) -> V2_FunctionDecorator: ...
@overload
def decorator(wrapper: ClassMethodWrapperFunction[P, R], /) -> V2_FunctionDecorator: ...
@overload
def decorator(
    wrapper: InstanceMethodWrapperFunction[P, R], /
) -> V2_FunctionDecorator: ...

# ... Positional arguments.

@overload
def decorator(
    *,
    enabled: bool | Boolean | Callable[[], bool] | None = None,
    adapter: str | FullArgSpec | AdapterFactory | Callable[..., Any] | None = None,
    proxy: type[V2_FunctionWrapper[Any, Any]] | None = None,
) -> V2_PartialFunctionDecorator: ...

# function_wrapper()

@overload
def function_wrapper(wrapper: type[Any]) -> V2_FunctionDecorator: ...
@overload
def function_wrapper(
    wrapper: GenericCallableWrapperFunction[P, R],
) -> V2_FunctionDecorator: ...
@overload
def function_wrapper(
    wrapper: ClassMethodWrapperFunction[P, R],
) -> V2_FunctionDecorator: ...
@overload
def function_wrapper(
    wrapper: InstanceMethodWrapperFunction[P, R],
) -> V2_FunctionDecorator: ...
