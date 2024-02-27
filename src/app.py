""" This module contains the App class which is the main class of the application. """

from helpers import Database, NokiaLocationRetrieval, NokiaLocationVerification
from report import Report
from user import User


class App:
    """Main class of the application."""

    def __init__(self, db: Database, user: User):
        self.db: Database = db
        self.user: User = user
        self.reports: list[Report] = self.get_close_reports(self.user, self.db)

    def add_user(self, name: str, mobile_number: int, location: tuple[float], is_admin: bool = False) -> User:
        """Add a user to the app."""
        user = User(name, mobile_number, location, is_admin)
        self.db.insert_user(user)
        return user

    def add_report(self, user, title, location, category, description, image, status="pending", bounty=0) -> Report:
        """Add a report to the app."""
        if not NokiaLocationVerification(user.mobile_number, location):
            return "Location not verified"

        report = user.report_issue(title, location, category, description, image, status, bounty)
        self.update_db(user, report)
        return report

    def get_close_reports(self, user, db) -> list[Report]:
        """Get the reports that are closed."""
        return [
            report
            for report in db.reports
            if self.in_radius(report.location, NokiaLocationRetrieval(user.mobile_number))
        ]  # TODO: Change this for a query that returns the reports that are closer than a radius

    def resolve_report(self, user: User, report: Report) -> None:
        """Add a report to the app."""
        user.resolve_report(report)
        self.update_db(user, report)

    def upvote(self, user: User, report: Report) -> None:
        """Upvote a report."""
        report.upvote()
        user.contribution_award(report)
        self.update_db(user, report)

    def downvote(self, user: User, report: Report) -> None:
        """Downvote a report."""
        report.downvote()
        user.contribution_award(report)
        self.update_db(user, report)

    def get_user(self, name: str) -> User:
        """Get a user from the app."""
        return self.db.get_user(name)

    def get_report(self, title: str) -> Report:
        """Get a report from the app."""
        return self.db.get_report(title)

    def update_db(self, user: User, report: Report) -> None:
        if isinstance(report, Report):
            self.db.update_report(report)
        if isinstance(user, User):
            self.db.update_user(user)

    def run(self) -> None:
        """Main game loop."""
        while True:
            self.get_actions()
            self.update()
            self.draw()

    def get_actions(self):
        pass  # Front-end, recieve user input and call the corresponding method

    def update(self):
        self.reports = self.get_close_reports(self.user, self.db)
        self.user = self.db.get_user(self.user.name)
        self.reports = self.db.get_report(self.reports.title)

    def draw(self):
        pass  # Front-end printing, with location and self.reports, self.db, self.user
