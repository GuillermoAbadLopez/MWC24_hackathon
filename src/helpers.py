"""Helper module for the app with database and APIs mocks."""


class NokiaLocationRetrieval:
    pass


class NokiaLocationVerification:
    pass


class Database:
    """Database class for the app."""

    def __init__(self):
        self.users = {}
        self.reports = {}

    def insert_user(self, user):
        """Insert a user to the database."""
        self.users[user.name] = user

    def insert_report(self, report):
        """Insert a report to the database."""
        self.reports[report.title] = report

    def update_report(self, report):
        """Update a report to the database."""
        if report.title in self.reports:
            self.reports[report.title] = report

    def get_user(self, name):
        """Get a user from the database."""
        return self.users.get(name)

    def get_report(self, title):
        """Get a report from the database."""
        return self.reports.get(title)
