""" Main file for the app."""

import pytest
from app import App
from helpers import Database

### MAIN LOOP APP:

if __name__ == "__main__":
    # Instantiate the database and the app
    db = Database()
    app = App(db)
    # app.run()

    ##############
    ### TEST 1 ###
    ##############
    # Original user closes an issue, trying upvotes before and after:
    report1 = app.add_report(
        user=app.user,
        location=(0, 0),
        category="",
        title="Issue 1",
        description="This is the first issue",
        image=None,
        status="pending",
        bounty=0,
    )

    assert report1.status == "pending"

    app.upvote(app.user, report1)

    assert report1.status == "active"

    app.downvote(app.user, report1)

    assert app.user.points == 3
    assert report1.upvotes == report1.downvotes == 1

    # User resolves the report
    app.resolve_report(app.user, report1)

    assert report1.status == "resolved"

    with pytest.raises(ValueError):
        # User upvotes a already closed report
        app.upvote(app.user, report1)

    with pytest.raises(ValueError):
        # User downvotes an already closed report
        app.downvote(app.user, report1)

    user = app.get_user("default")
    report = app.get_report("Issue 1")

    assert report == report1
    assert user.name == "default"

    ##############
    ### TEST 2 ###
    ##############
    # Another user tries to close an issue, then it gets closed by downvotes / bounty

    app.user.points = 100  # Manual set for testing purposes

    report2 = app.add_report(
        user=app.user,
        location=(0, 0),
        category="",
        title="Issue 2",
        description="This is the second issue",
        image=None,
        bounty=10,
    )

    assert user.points == 91

    app.add_user(name="default2", mobile_number=10000, location=(0, 0))

    with pytest.raises(ValueError):
        # User2 tries to resolve a report, that is not his
        app.resolve_report(app.get_user("default2"), report2)

    assert report2.status == "pending"

    for i in range(5):
        app.downvote(app.user, report2)

    assert user.points == 101
    assert report2.status == "resolved"

    with pytest.raises(ValueError):
        app.downvote(app.user, report2)
