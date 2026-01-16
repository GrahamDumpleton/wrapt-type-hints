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

test: test-mypy test-pyrefly test-pyright test-ty

clean:
    rm -rf .mypy_cache
    rm -rf .venv
