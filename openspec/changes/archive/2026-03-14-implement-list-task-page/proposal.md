## Why

Users need a central view to see all their tasks, track their status, and manage their productivity.

## What Changes

- Implement a Django ListView to display `Todo` objects.
- Create an HTML template to render the list with modern aesthetics.
- Add a URL route for the task list page.
- Update the home view or root URL to point to the task list.

## Capabilities

### New Capabilities
- `task-listing`: Ability to view a paginated list of all created todo items.

## Impact

- `app/views/list.py`: [NEW] Implementation of the task list view.
- `app/templates/app/list.html`: [NEW] Modern template for displaying tasks.
- `config/urls.py`: Add route for the task list.
