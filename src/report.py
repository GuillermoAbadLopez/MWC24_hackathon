"""Report module for the app."""

from ideas.copilot_suggestions.fourth import User


class Report:
    """Report class for the app."""

    def __init__(
        self,
        id: int,
        title: str,
        user: User,
        location: tuple[float],
        category: str,
        description: str = "",
        image: "Image" = None,
        status: str = "pending",
        bounty: int = 0,
    ):
        self.id: int = id
        self.title: str = title
        self.user: User = user
        self.location: tuple[float] = location  # bus, metro, bicycles, rentHousing, pets, parking, garbage, trees,
        # publicSpaces, commerce, infrastructure, noOrBadSignal, air, water, noise, soil, security, other
        self.category: str = category
        self.status: str = status  # pending, active and resolved
        self.bounty: int = bounty
        self.description: str = description
        self.image: "Image" = image
        self.upvotes: int = 0
        self.downvotes: int = 0

    def close(self) -> None:
        """Close the report."""
        self.status = "resolved"

    def upvote(self) -> None | str:
        """Upvote the report."""
        if self.status == "pending":
            self.status = "active"
        if self.status == "resolved":
            return "You can't upvote a resolved report"
        self.upvotes += 1

    def downvote(self) -> None | str:
        """Downvote the report."""
        if self.status == "resolved":
            return "You can't upvote a resolved report"
        self.downvotes += 1
        if self.downvotes - self.upvotes >= 5:
            self.close()

    def __str__(self) -> str:
        return f"Report: {self.title}, Bounty: {self.bounty}, Upvotes: {self.upvotes}, Downvotes: {self.downvotes}, Resolutions: {len(self.resolutions)}, Closed: {self.closed}"
