## Context

We are building a foundational Todo list application starting with the data layer.

## Goals

- Implement a robust `Todo` model.
- Enable basic task storage with metadata.
- Follow a scalable package structure for models and tests.

## Decisions

### Decision 1: Model Package Structure

Per user request, we will not use a single `models.py`. Instead:
- `app/models/` will be a package.
- `app/models/todo.py` will contain the `Todo` model.
- `app/models/__init__.py` will export `Todo`.

### Decision 2: Test Package Structure

Similarly for tests:
- `app/tests/` will be a package.
- `app/tests/test_todo.py` will contain unit tests for the `Todo` model.

### Decision 3: Field Selection

- `title`: `CharField(max_length=255)` - Scalable for most todo item titles.
- `description`: `TextField(blank=True)` - Optional detailed description.
- `completed`: `BooleanField(default=False)` - Simple status tracking.
- `created_at`: `DateTimeField(auto_now_add=True)` - Immutable creation timestamp.
