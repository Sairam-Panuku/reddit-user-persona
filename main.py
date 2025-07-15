import praw
from dotenv import load_dotenv
import os
import re
import warnings
import json

from generate_persona import extract_persona_data
from generate_html_profile import generate_html

warnings.filterwarnings("ignore", category=RuntimeWarning)

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    username=os.getenv("REDDIT_USERNAME"),
    password=os.getenv("REDDIT_PASSWORD"),
    user_agent=os.getenv("REDDIT_USER_AGENT")
)

os.makedirs("outputs/text_output", exist_ok=True)
os.makedirs("outputs/json_output", exist_ok=True)
os.makedirs("outputs/html_output", exist_ok=True)

def extract_username_from_url(url):
    match = re.search(r"reddit\.com/user/([\w\-_.]+)", url)
    return match.group(1) if match else url

def save_user_data(username, posts, comments):
    file_path = f"outputs/text_output/{username}.txt"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"Reddit User: u/{username}\n")
        f.write("=" * 60 + "\n\n")

        f.write("Posts:\n")
        f.write("-" * 60 + "\n")
        for i, post in enumerate(posts, 1):
            f.write(f"[Post {i}]\n")
            f.write(f"Subreddit: {post['subreddit']}\n")
            f.write(f"Title: {post['title']}\n")
            f.write(f"Body: {post['body']}\n")
            f.write(f"URL: {post['url']}\n")
            f.write(f"Score: {post['score']}\n")
            f.write("-" * 60 + "\n\n")

        f.write("\nComments:\n")
        f.write("-" * 60 + "\n")
        for i, comment in enumerate(comments, 1):
            f.write(f"[Comment {i}]\n")
            f.write(f"Subreddit: {comment['subreddit']}\n")
            f.write(f"Body: {comment['body']}\n")
            f.write(f"Score: {comment['score']}\n")
            f.write("-" * 60 + "\n\n")

    print(f"✅ Data saved to {file_path}")
    return file_path 

def fetch_user_content(username, post_limit=50, comment_limit=50):
    posts, comments = [], []
    try:
        redditor = reddit.redditor(username)

        for submission in redditor.submissions.new(limit=post_limit):
            posts.append({
                "title": submission.title,
                "body": submission.selftext,
                "url": submission.url,
                "score": submission.score,
                "subreddit": str(submission.subreddit)
            })

        for comment in redditor.comments.new(limit=comment_limit):
            comments.append({
                "body": comment.body,
                "score": comment.score,
                "subreddit": str(comment.subreddit)
            })

    except Exception as e:
        print(f"❌ Error fetching content for user '{username}': {e}")

    return posts, comments

def test_connection():
    print("✅ Authenticated as:", reddit.user.me())

if __name__ == "__main__":
    test_connection()

    input_users = [
        "https://www.reddit.com/user/biswassumit25/",
        "https://www.reddit.com/user/Any_Track_1781/",
        "https://www.reddit.com/user/Character_Market8330/",
        "https://www.reddit.com/user/JyotiIsMine/",
        "https://www.reddit.com/user/Unidan/"
    ]

    for url in input_users:
        user = extract_username_from_url(url)
        print(f"\n🚀 Processing u/{user}...")
        posts, comments = fetch_user_content(user)
        print(f"📥 Fetched {len(posts)} posts and {len(comments)} comments")

        # Save raw content
        txt_path = save_user_data(user, posts, comments)

        # Extract persona info
        persona_data = extract_persona_data(txt_path)

        #  Save JSON persona
        json_path = f"outputs/json_output/{user}_persona.json"
        with open(json_path, "w", encoding="utf-8") as f:
            json.dump(persona_data, f, indent=2)
        print(f"✅ Persona saved to {json_path}")

        #  Generate HTML profile
        html_path = f"outputs/html_output/{user}_profile.html"
        generate_html(user, persona_data, html_path)
        print(f"🎨 HTML saved to {html_path}")
