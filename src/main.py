""" Main file for the app."""

from app import App


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


# Instantiate the database and the app
db = Database()
app = App(db)

# User reports an issue
report1 = app.add_report(app.user, "Issue 1", "This is the first issue", 10)

# User resolves the report
app.resolve_report(app.user, report1)

# User upvotes the report
app.upvote(app.user, report1)

# User downvotes the report
app.downvote(app.user, report1)
