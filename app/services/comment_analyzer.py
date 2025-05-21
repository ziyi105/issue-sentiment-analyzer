# analyzer/comment_analysis_pipeline.py

from typing import Dict
from services.clusterer.KMeansClusterer import KMeansClusterer
from services.summarizer.Summarizer import Summarizer


class CommentAnalyzer:
    def __init__(self, comment_file: str, num_clusters: int = 3):
        self.comment_file = comment_file
        self.num_clusters = num_clusters
        self.clusterer = KMeansClusterer(num_clusters=num_clusters)
        self.summarizer = Summarizer()

    def load_comments(self) -> list:
        with open(self.comment_file, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f if line.strip()]

    def analyze(self) -> Dict[int, str]:
        print("📥 Loading comments...")
        comments = self.load_comments()

        print("🔀 Clustering comments...")
        clustered_comments = self.clusterer.cluster(comments)

        print("📝 Summarizing each cluster...")
        summaries = {}
        for cluster_id, cluster in clustered_comments.items():
            print(f"\n📚 Cluster {cluster_id + 1} ({len(cluster)} comments):")
            summary = self.summarizer.summarize_cluster(cluster)
            summaries[cluster_id] = summary
            print(summary)

        return summaries
