from sentence_transformers import SentenceTransformer
from sklearn.cluster import KMeans
from typing import List, Dict
import numpy as np


class KMeansClusterer:
    def __init__(self, model_name: str = 'all-MiniLM-L6-v2', num_clusters: int = 3):
        """
        :param model_name: Pretrained SentenceTransformer model name
        :param num_clusters: Number of clusters (K for KMeans)
        """
        self.model_name = model_name
        self.num_clusters = num_clusters
        self.model = SentenceTransformer(model_name)
        self.kmeans = None
        self.labels = None

    def embed_comments(self, comments: List[str]) -> np.ndarray:
        """Converts comments into embeddings."""
        return self.model.encode(comments)

    def cluster(self, comments: List[str]) -> Dict[int, List[str]]:
        """Performs KMeans clustering on the comments."""
        embeddings = self.embed_comments(comments)
        self.kmeans = KMeans(n_clusters=self.num_clusters, random_state=42)
        self.labels = self.kmeans.fit_predict(embeddings)

        clustered = {}
        for label, comment in zip(self.labels, comments):
            clustered.setdefault(label, []).append(comment)
        return clustered

    def get_cluster_centroids(self) -> np.ndarray:
        """Returns the cluster centers (centroids) if available."""
        if self.kmeans:
            return self.kmeans.cluster_centers_
        else:
            raise ValueError("Model not yet fitted. Call `cluster()` first.")
