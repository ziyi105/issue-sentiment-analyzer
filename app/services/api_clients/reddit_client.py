# api_clients/reddit_client.py
import praw
from services.secrets import CLIENT_ID, CLIENT_SECRET, USER_AGENT


class RedditClient:
    def __init__(self):
        """Initialize the Reddit client with credentials."""
        self.reddit = praw.Reddit(
            client_id=CLIENT_ID,
            client_secret=CLIENT_SECRET,
            user_agent=USER_AGENT,
        )

    def fetch_comments(self, subreddit_name: str, limit: int = 1) -> list[str]:
        """
        Fetch comments from the top posts of a subreddit.

        Args:
            subreddit_name (str): The name of the subreddit to fetch comments from.
            limit (int): The number of top posts to fetch.

        Returns:
            list[str]: A list of comments from the subreddit.
        """
        comments = []
        subreddit = self.reddit.subreddit(subreddit_name)
        for submission in subreddit.top(limit=limit):
            print(f"Title: {submission.title}")
            submission.comments.replace_more(limit=0)
            for comment in submission.comments.list():
                comments.append(comment.body)
        return comments
