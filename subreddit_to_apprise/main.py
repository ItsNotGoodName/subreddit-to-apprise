import os
import time

import praw
import dotenv
import apprise


def main():
    dotenv.load_dotenv()

    # Subreddit limit
    limit = 5
    if os.getenv("LIMIT") is not None:
        limit = int(os.getenv("LIMIT"))

    # Fetch interval
    interval = 60
    if os.getenv("INTERVAL") is not None:
        interval = int(os.getenv("INTERVAL"))

    # Apprise setup
    rise = apprise.Apprise()
    if os.getenv("APPRISE_URLS") is not None:
        urls = os.getenv("APPRISE_URLS").split(" ")
        for url in urls:
            rise.add(url)

    # Reddit setup
    reddit = praw.Reddit(
        client_id=os.getenv("CLIENT_ID"),
        client_secret=os.getenv("CLIENT_SECRET"),
        user_agent="subreddit-to-apprise",
    )
    subreddit = reddit.subreddit(os.getenv("SUBREDDITS"))

    # Get new posts
    last_posts = []
    for post in subreddit.new(limit=limit):
        last_posts.append(post)
    print("Started")

    while True:
        time.sleep(interval)

        # Get new posts
        posts = []
        for post in subreddit.new(limit=limit):
            posts.append(post)

        # Get new posts in old to new order
        new_posts = []
        for post in posts:
            if post in last_posts:
                break

            new_posts.append(post)
        new_posts.reverse()

        print(f"{len(new_posts)} new posts")

        # Notify
        for post in new_posts:
            body = "https://old.reddit.com" + post.permalink
            print(f"{post.title} - {body}")
            if post.url != post.permalink:
                body += "\n" + post.url
            rise.notify(title=post.title, body=body)

        last_posts = posts
