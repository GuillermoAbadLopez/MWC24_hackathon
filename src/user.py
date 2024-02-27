"""User module for the app."""

import numpy as np
from report import Report


class User:
    """User class for the app."""

    def __init__(self, name: str, mobile_number: int, location: tuple[float], is_admin: bool = False):
        self.name: str = name
        self.is_admin: bool = is_admin
        self.points: int = 0
        self.mobile_number: int = mobile_number
        self.location: tuple[float] = location

    def report_issue(self, title, location, category, description, image, status="pending", bounty=0) -> Report | str:
        """Report an issue."""
        if self.points < bounty:
            return "Not enough points to set this bounty"

        self.points -= bounty
        return Report(
            id=np.random.randint(),
            title=title,
            user=self,
            location=location,
            category=category,
            description=description,
            image=image,
            status=status,
            bounty=bounty,
        )

    def resolve_report(self, report: Report) -> str | None:
        if not report.user == self and not self.is_admin:
            return "Only the user who created the report or admin users can resolve the report"

        report.status = "resolved"

    def contribution_award(self, report: Report) -> None:
        """Upvote/downvote report award."""
        self.points += 1
        self.points += report.bounty // 10

    def __str__(self) -> str:
        return f"User: {self.name}, Points: {self.points}"
