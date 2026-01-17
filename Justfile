default:
    @just --list

init:
    uv sync

test-mypy:
    uv run mypy tests

test-pyrefly:
    uv run pyrefly check tests

test-pyright:
    uv run pyright tests

test-ty:
    uvx ty check tests

test:
    -uv run mypy tests
    -uv run pyrefly check tests
    -uv run pyright tests
    -uv run ty check tests

clean:
    rm -rf .mypy_cache
    rm -rf .venv
