# task-storage Specification

## Purpose
TBD - created by archiving change create-todo-model. Update Purpose after archive.
## Requirements
### Requirement: Todo Storage

The system MUST allow storing todo items with a title, optional description, completion status, and creation timestamp.

#### Scenario: Create a new todo item

- **WHEN** a user creates a todo item with a title and description
- **THEN** the item is saved to the database
- **AND** the `completed` flag is set to `False` by default
- **AND** the `created_at` timestamp is automatically set to the current time

#### Scenario: Mark todo as completed

- **WHEN** a user updates a todo item's `completed` flag to `True`
- **THEN** the item's status is updated in the database

