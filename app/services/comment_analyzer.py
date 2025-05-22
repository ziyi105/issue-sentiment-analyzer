# analyzer/comment_analysis_pipeline.py

from typing import Dict, List
from services.clusterer.KMeansClusterer import KMeansClusterer
from services.summarizer.Summarizer import Summarizer
from services.api_clients.reddit_client import RedditClient


class CommentAnalyzer:
    def __init__(self, num_clusters: int = 3):
        """
        Initialize the CommentAnalyzer.

        Args:
            num_clusters (int): The number of clusters for clustering comments.
            comment_file (str): Path to the text file containing comments (optional).
        """
        self.num_clusters = num_clusters
        self.clusterer = KMeansClusterer(num_clusters=num_clusters)
        self.summarizer = Summarizer()
        self.reddit_client = RedditClient()

    def load_comments_from_file(self, comment_file: str) -> List[str]:
        """
        Load comments from a text file.

        Returns:
            List[str]: A list of comments from the file.
        """
        with open(comment_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]

    def load_comments_from_reddit(self, subreddit: str, limit: int = 100) -> List[str]:
        """
        Fetch comments from a subreddit using the Reddit client.

        Args:
            subreddit (str): The name of the subreddit to fetch comments from.
            limit (int): The number of top posts to fetch.

        Returns:
            List[str]: A list of comments from the subreddit.
        """
        return self.reddit_client.fetch_comments(subreddit_name=subreddit, limit=limit)

    def analyze(self, source: str, subreddit: str = None, limit: int = 100, comment_file: str = None) -> Dict[int, str]:
        """
        Analyze comments from the specified source.

        Args:
            source (str): The source of comments ('txt' or 'reddit').
            subreddit (str): The subreddit to fetch comments from (required if source is 'reddit').
            limit (int): The number of top posts to fetch (used if source is 'reddit').

        Returns:
            Dict[int, str]: A dictionary of cluster IDs and their summaries.
        """
        print("📥 Loading comments...")
        if source == "txt":
            if not comment_file:
                raise ValueError("Comment file path must be provided for 'txt' source.")
            comments = self.load_comments_from_file(comment_file=comment_file)
        elif source == "reddit":
            if not subreddit:
                raise ValueError("Subreddit name must be provided for 'reddit' source.")
            comments = self.load_comments_from_reddit(subreddit=subreddit, limit=limit)
        else:
            raise ValueError("Invalid source. Use 'txt' or 'reddit'.")

        print("🔀 Clustering comments...")
        clustered_comments = self.clusterer.cluster(comments)
        print(f"🔍 Found {len(clustered_comments)} clusters.")

        print("📝 Summarizing each cluster...")
        summaries = {}
        for cluster_id, cluster in clustered_comments.items():
            if cluster_id not in summaries:  # Prevent duplicate summarization
                print(f"\n📚 Cluster {cluster_id} ({len(cluster)} comments):")
                summary = self.summarizer.summarize_cluster(cluster)
                summaries[cluster_id] = summary
                print(summary)

        return summaries
