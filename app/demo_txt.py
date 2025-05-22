from services.comment_analyzer import CommentAnalyzer

if __name__ == "__main__":
    analyzer = CommentAnalyzer(comment_file="dataset/home-based-classes.txt", num_clusters=3)
    summaries = analyzer.analyze()
