## ADDED Requirements

### Requirement: Task Listing

The system MUST allow users to view a list of all existing todo items.

#### Scenario: View all tasks

- **WHEN** a user navigates to the tasks page
- **THEN** the system MUST display all `Todo` items from the database
- **AND** each item MUST show its title, completed status, and creation date
- **AND** items SHOULD be ordered by `created_at` in descending order (newest first)
