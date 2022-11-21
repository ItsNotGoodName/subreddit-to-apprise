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

    # Get newest post
    last_post = ""
    posts = subreddit.new(limit=1)
    for post in posts:
        last_post = str(post)
    print("Started")
    time.sleep(interval)

    while True:
        posts = subreddit.new(limit=limit)

        # Get new posts in reverse order
        new_posts = []
        for post in posts:
            if str(post) == last_post:
                break

            new_posts.append(post)
        new_posts.reverse()

        print(f"{len(new_posts)} new posts")

        # Notify
        for post in new_posts:
            body = "https://reddit.com/" + post.permalink
            if post.url != post.permalink:
                body += "\n" + post.url

            print(f"{post.title} - {body}")
            rise.notify(title=post.title, body=body)

        if len(new_posts) != 0:
            last_post = str(new_posts[-1])

        time.sleep(interval)
