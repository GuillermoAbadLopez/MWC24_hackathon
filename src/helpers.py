"""Helper module for the app with database and APIs mocks."""

from ideas.copilot_suggestions.fourth import Report, User


class NokiaLocationRetrieval:
    pass


class NokiaLocationVerification:
    pass


class Database:
    """Database class for the app."""

    def __init__(self):
        self.users: dict[str, User] = {}
        self.reports: dict[str, Report] = {}

    def insert_user(self, user: User):
        """Insert a user to the database."""
        self.users[user.name] = user

    def insert_report(self, report: Report):
        """Insert a report to the database."""
        self.reports[report.title] = report

    def update_report(self, report: Report):
        """Update a report to the database."""
        if report.title in self.reports:
            self.reports[report.title] = report

    def get_user(self, name: str):
        """Get a user from the database."""
        return self.users.get(name)

    def get_report(self, title: str):
        """Get a report from the database."""
        return self.reports.get(title)
