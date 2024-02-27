""" This module contains the App class which is the main class of the application. """

from report import Report
from user import User


class App:
    """Main class of the application."""

    def __init__(self, db):
        self.db = db
        self.user = self.add_user("Alice")

    def add_user(self, name, is_admin=False):
        """Add a user to the app."""
        user = User(name, is_admin)
        self.db.insert_user(user)
        return user

    def add_report(self, user, title, content, bounty):
        """Add a report to the app."""
        report = user.report_issue(title, content, bounty)
        self.update_db(user, report)
        return report

    def resolve_report(self, user, report):
        """Add a report to the app."""
        user.resolve_report(report)
        self.update_db(user, report)

    def upvote(self, user, report):
        """Upvote a report."""
        user.upvote(report)
        self.update_db(user, report)

    def downvote(self, user, report):
        """Downvote a report."""
        user.upvote(report)
        self.update_db(user, report)

    def get_user(self, name):
        """Get a user from the app."""
        return self.db.get_user(name)

    def get_report(self, title):
        """Get a report from the app."""
        return self.db.get_report(title)

    def update_db(self, user, report):
        if isinstance(report, Report):
            self.db.update_report(report)
        if isinstance(user, User):
            self.db.update_user(user)
