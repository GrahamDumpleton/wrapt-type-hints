from inspect import FullArgSpec
from typing import Any, Callable, Concatenate, overload

from wrapt import (AdapterFactory, Boolean, ClassMethodWrapperFunction,
                   Descriptor, FunctionWrapper, GenericCallableWrapperFunction,
                   InstanceMethodWrapperFunction, P, PartialFunctionDecorator,
                   R, T)

class V1_FunctionDecorator:

    @overload
    def __call__(
        self,
        callable: Callable[P, R]
                | Callable[Concatenate[type[T], P], R]
                # | Callable[Concatenate[Any, P], R] # Don't use, breaks mypy.
                | Callable[[type[T]], R]
    ) -> FunctionWrapper[P, R]: ...
    @overload
    def __call__(
        self,
        callable: Descriptor
    ) -> FunctionWrapper[P, Any]: ...

class V1_PartialFunctionDecorator:
    @overload
    def __call__(
        self, wrapper: GenericCallableWrapperFunction[P, R], /
    ) -> V1_FunctionDecorator: ...
    @overload
    def __call__(
        self, wrapper: ClassMethodWrapperFunction[P, R], /
    ) -> V1_FunctionDecorator: ...
    @overload
    def __call__(
        self, wrapper: InstanceMethodWrapperFunction[P, R], /
    ) -> V1_FunctionDecorator: ...

# ... Decorator applied to class type.

@overload
def decorator(wrapper: type[T], /) -> V1_FunctionDecorator: ...

# ... Decorator applied to function or method.

@overload
def decorator(
    wrapper: GenericCallableWrapperFunction[P, R], /
) -> V1_FunctionDecorator: ...
@overload
def decorator(
    wrapper: ClassMethodWrapperFunction[P, R], /
) -> V1_FunctionDecorator: ...
@overload
def decorator(
    wrapper: InstanceMethodWrapperFunction[P, R], /
) -> V1_FunctionDecorator: ...
# ... Positional arguments.

@overload
def decorator(
    *,
    enabled: bool | Boolean | Callable[[], bool] | None = None,
    adapter: str | FullArgSpec | AdapterFactory | Callable[..., Any] | None = None,
    proxy: type[FunctionWrapper[Any, Any]] | None = None,
) -> PartialFunctionDecorator: ...
