from langchain.tools import tool
import praw
import os

@tool
def reddit_tool(query: str):
    """
    Searches Reddit and returns top relevant posts (title, score, url).
    """
    reddit = praw.Reddit(
        client_id=os.getenv("REDDIT_CLIENT_ID"),
        client_secret=os.getenv("REDDIT_SECRET"),
        user_agent="agent-system"
    )

    posts = []

    for post in reddit.subreddit("all").search(query, limit=5):
        posts.append({
            "title": post.title,
            "score": post.score,
            "url": post.url
        })

    return posts