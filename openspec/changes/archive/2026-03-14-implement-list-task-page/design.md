## Context

We have the `Todo` model implemented. Now we need a user-facing page to list these tasks.

## Goals

- Create a clean, responsive task list page.
- Use Django's `ListView` for efficiency.
- Follow the project's package structure for views.

## Non-Goals

- Editing or deleting tasks (will be handled in separate changes).
- User authentication (out of scope for now).

## Decisions

### Decision 1: View Package Structure

The user wants separate files. I will create `app/views/list.py` for the list view.

### Decision 2: Template Location

Standard Django practice: `app/templates/app/list.html`.

### Decision 3: Styling

I will use a premium design with:
- A clean dark mode or soft light mode palette.
- Hover effects for task items.
- A "glassmorphism" style container for the list.

### Decision 4: Ordering

Tasks will be ordered by `created_at` descending as per spec.

## Risks / Trade-offs

- **Performance**: For very large lists, we might need pagination. I'll include basic pagination in the design (e.g., 20 items per page).
