wrapt-type-hints
================

This code repository contains tests for `wrapt` type hints. It's purpose is to
compare the results from running `mypy`, `pyrefly`, `pyright` and `ty` with the
goal of working out a set of type hints for `wrapt` which work with all these
tools, or identify issues with the tools so bugs can be reported.

To test out different implementations for type hints for `wrapt`, create a new
file with name in form `versions/wrapt_type_hints_v?.pyi`. Then modify
`versions/wrapt.pyi` to refer to the new version. The new type hints file could
be a complete standalone implementation, or could build on and replace parts of
the original `wrapt` version. For examples see existing versions in the
directory.

To initialize ready for testing run:

```
uv sync
```

Then run any of:

```
just test-mypy
just test-prefly
just test-pyright
just test-ty
```

To clean up, run:

```
just clean
```
