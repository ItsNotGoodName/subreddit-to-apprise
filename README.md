# subreddit-to-apprise

Send new posts from subreddits to Apprise URLs.

## Environment Variables

| Name          | Default | Required | Description                                                                                            |
| ------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------ |
| CLIENT_ID     |         | Yes      | App id from https://www.reddit.com/prefs/apps/                                                         |
| CLIENT_SECRET |         | Yes      | App secret from https://www.reddit.com/prefs/apps/                                                     |
| SUBREDDITS    |         | Yes      | One more subreddits seperated by + signs                                                               |
| LIMIT         | 5       |          | How man posts to fetch on each refresh                                                                 |
| INTERVAL      | 60      |          | Interval in seconds between each refresh                                                               |
| APPRISE_URLS  |         |          | [Apprise URLs](https://github.com/caronc/apprise#productivity-based-notifications) seperated by spaces |

## Config

The program looks for a `.env` file in the current directory.
