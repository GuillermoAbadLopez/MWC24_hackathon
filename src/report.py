"""Report module for the app."""


class Report:
    """Report class for the app."""

    def __init__(self, title, content, user, bounty, location):
        self.title = title
        self.content = content
        self.user = user
        self.bounty = bounty
        self.upvotes = 0
        self.downvotes = 0
        self.closed = False
        self.location = location

    def close(self):
        """Close the report."""
        self.closed = True

    def __str__(self):
        return f"Report: {self.title}, Bounty: {self.bounty}, Upvotes: {self.upvotes}, Downvotes: {self.downvotes}, Resolutions: {len(self.resolutions)}, Closed: {self.closed}"
