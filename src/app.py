""" This module contains the App class which is the main class of the application. """

from helpers import NokiaLocationRetrieval, NokiaLocationVerification
from report import Report
from user import User


class App:
    """Main class of the application."""

    def __init__(self, db):
        self.db = db
        self.user = self.add_user("Alice")
        self.reports = self.get_close_reports(self.user, self.db)

    def add_user(self, name, is_admin=False):
        """Add a user to the app."""
        user = User(name, is_admin)
        self.db.insert_user(user)
        return user

    # TODO:  Where should we do this? In the app or in the user?
    def add_report(self, user, title, content, bounty, location):
        """Add a report to the app."""
        if NokiaLocationVerification(user.mobile_number, location):
            report = user.report_issue(title, content, bounty)
            self.update_db(user, report)
            return report
        else:
            return "Location not verified"

    # TODO: When to call this?
    def get_close_reports(self, user, db):
        """Get the reports that are closed."""
        return [
            report
            for report in db.reports
            if self.in_radius(report.location, NokiaLocationRetrieval(user.mobile_number))
        ]  # Change this for a query that returns the reports that are closer than a radius

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

    def run(self):
        """Main game loop."""
        while True:
            self.update()
            self.draw()

    def update(self):
        self.reports = self.get_close_reports(self.user, self.db)
        self.user = self.db.get_user(self.user.name)
        self.reports = self.db.get_report(self.reports.title)

    def draw(self):
        pass  # Front end printing, with location and self.reports, self.db, self.user
