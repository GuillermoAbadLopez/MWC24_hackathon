""" Main file for the app."""

from app import App
from helpers import Database

### MAIN LOOP APP:

if __name__ == "__main__":
    # Instantiate the database and the app
    db = Database()
    app = App(db)
    app.run()


### EXAMPLES OF CALLS COMING FROM THE APP, while the app run method:

# User reports an issue
report1 = app.add_report(
    user=app.user,
    location=(0, 0),
    category="",
    title="Issue 1",
    description="This is the first issue",
    image=None,
    status="pending",
    bounty=10,
)

# User resolves the report
app.resolve_report(app.user, report1)

# User upvotes the report
app.upvote(app.user, report1)

# User downvotes the report
app.downvote(app.user, report1)

user = app.get_user("default")
report = app.get_report("Issue 1")

assert report == report1
