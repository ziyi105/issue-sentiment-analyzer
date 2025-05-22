import argparse
from services.comment_analyzer import CommentAnalyzer

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run the Comment Analyzer.")
    parser.add_argument(
        "--source", 
        type=str, 
        required=True, 
        choices=["reddit", "txt"], 
        help="Specify the source of comments: 'reddit' or 'txt'."
    )
    parser.add_argument(
        "--subreddit", 
        type=str, 
        help="The subreddit to fetch comments from (required if source is 'reddit')."
    )
    parser.add_argument(
        "--file", 
        type=str, 
        help="The path to the text file containing comments (required if source is 'txt')."
    )
    parser.add_argument(
        "--clusters", 
        type=int, 
        default=3, 
        help="The number of clusters for comment analysis (default: 3)."
    )
    parser.add_argument(
        "--limit", 
        type=int, 
        default=1, 
        help="The number of top posts to fetch from Reddit (default: 100)."
    )

    args = parser.parse_args()

    # Validate arguments
    if args.source == "reddit" and not args.subreddit:
        parser.error("--subreddit is required when source is 'reddit'.")
    if args.source == "txt" and not args.file:
        parser.error("--file is required when source is 'txt'.")

    analyzer = CommentAnalyzer()
    summaries = analyzer.analyze(source=args.source, subreddit=args.subreddit, limit=args.limit, comment_file=args.file)

if __name__ == "__main__":
    main()

# python app/run_comment_analyzer.py --source txt --file dataset/home-based-classes.txt --clusters 3
# python app/run_comment_analyzer.py --source reddit --subreddit malaysia --clusters 3 --limit 1