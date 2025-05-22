# Issue Sentiment Analyzer

The **Issue Sentiment Analyzer** is a thematic sentiment analysis tool designed to analyze public opinion on news issues. It retrieves comments from Reddit or a text file, clusters them into groups based on similarity, and summarizes the main opinions and sentiments expressed in each cluster.

## Features
- Fetch comments from Reddit using the Reddit API.
- Cluster comments using KMeans clustering.
- Summarize clusters using a language model (e.g., Ollama).
- Supports both Reddit and text file inputs.

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd issue-sentiment-analyzer
```

### 2. Install Dependencies
Make sure you have Python 3.10 or higher installed. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Create a secrets.py File
Create a 'secrets.py' file in the 'app/services' directory to store your Reddit API credentials:
```bash
# filepath: [secrets.py](http://_vscodecontentref_/1)
CLIENT_ID = "your_reddit_client_id"
CLIENT_SECRET = "your_reddit_client_secret"
USER_AGENT = "your_user_agent"
```
You can obtain these credentials by creating a Reddit app at Reddit Apps.

## How to Run
### 1. Run with a Text File as Input
To analyze comments from a text file, use the following command:
```bash
python [run_comment_analyzer.py](http://_vscodecontentref_/2) --source txt --file dataset/comments.txt --clusters 3
```
`--source txt`: Specifies that the input is a text file.
`--file dataset`/comments.txt: Path to the text file containing comments.
`--clusters 3`: Number of clusters for analysis

### 2. Run with Reddit as Input
To analyze comments from a subreddit, use the following command:
```bash
python [run_comment_analyzer.py](http://_vscodecontentref_/3) --source reddit --subreddit malaysia --clusters 3 --limit 50
```
`--source reddit`: Specifies that the input is from Reddit.
`--subreddit malaysia`: Name of the subreddit to fetch comments from.
`--clusters 3`: Number of clusters for analysis.
`--limit 50`: Number of top posts to fetch from the subreddit.

## Example Output
When you run the analyzer, you will see output like this:
```bash
📥 Loading comments...
🔀 Clustering comments...
🔍 Found 3 clusters.
📝 Summarizing each cluster...

📚 Cluster 1 (80 comments):
The story is about the author's childhood memories in Malaysia...

📚 Cluster 2 (73 comments):
The text discusses the smell of different foods...

📚 Cluster 3 (43 comments):
The main opinion expressed in the comments is that they are positive...
```

## Project Structure
```bash
issue-sentiment-analyzer/
│
├── app/
│   ├── run_comment_analyzer.py       # Main script to run the analyzer
│   ├── services/
│   │   ├── api_clients/
│   │   │   └── reddit_client.py      # Fetches comments from Reddit
│   │   ├── clusterer/
│   │   │   └── KMeansClusterer.py    # Clusters comments using KMeans
│   │   ├── summarizer/
│   │   │   └── summarizer.py         # Summarizes clusters
│   │   ├── [comment_analyzer.py](http://_vscodecontentref_/4)       # Combines all components
│   │   └── secrets.py                # Stores Reddit API credentials
│   └── dataset/
│       └── comments.txt              # Example text file with comments
│
└── requirements.txt                  # Python dependencies
```