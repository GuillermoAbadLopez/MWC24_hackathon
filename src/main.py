""" Main file for the app."""

from app import App
from dbs_and_apis import Database

### MAIN LOOP APP:

if __name__ == "__main__":
    # Instantiate the database and the app
    db = Database()
    app = App(db)
    app.run()


### EXAMPLES OF CALLS COMING FROM THE APP, while the app run method:

# User reports an issue
report1 = app.add_report(app.user, "Issue 1", "This is the first issue", 10)

# User resolves the report
app.resolve_report(app.user, report1)

# User upvotes the report
app.upvote(app.user, report1)

# User downvotes the report
app.downvote(app.user, report1)
