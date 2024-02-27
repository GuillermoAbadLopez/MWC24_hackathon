"""User module for the app."""

from main import NokiaLocationRetrieval, NokiaLocationVerification
from report import Report


class User:
    """User class for the app."""

    def __init__(self, name, mobile_number, is_admin=False):
        self.name = name
        self.is_admin = is_admin
        self.points = 0
        self.mobile_number = mobile_number
        self.location = None

    def report_issue(self, title, content, bounty, location):
        """Report an issue."""
        if NokiaLocationVerification(self.mobile_number, location):
            return Report(title, content, self, bounty)
        if self.points >= bounty:
            self.points -= bounty
            return Report(title, content, self, bounty)
        else:
            return "Not enough points to set this bounty"

    def resolve_report(self, report):
        if report.user == self or self.is_admin:
            report.closed = True
        else:
            return "Only the user who created the report or admin users can resolve the report"

    def upvote(self, report):
        """Upvote a report."""
        report.upvotes += 1
        self.points += 1
        self.points += report.bounty // 10

    def downvote(self, report):
        """Downvote a report."""
        report.downvotes += 1
        self.points -= 1
        if report.downvotes - report.upvotes >= 5:
            report.close()
        self.points += report.bounty // 10

    def get_close_reports(self, db):
        """Get the reports that are closed."""
        return [
            report
            for report in db.reports
            if self.in_radius(report.location, NokiaLocationRetrieval(self.mobile_number))
        ]  # Change this for a query that returns the reports that are closer than a radius

    def __str__(self):
        return f"User: {self.name}, Points: {self.points}"
