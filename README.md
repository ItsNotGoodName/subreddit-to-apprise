# subreddit-to-apprise

Send new posts from subreddits to Apprise URLs.

# Environment Variables

| Name          | Default | Required | Description                                                                                            |
| ------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------ |
| CLIENT_ID     |         | Yes      | App id from https://www.reddit.com/prefs/apps/                                                         |
| CLIENT_SECRET |         | Yes      | App secret from https://www.reddit.com/prefs/apps/                                                     |
| SUBREDDITS    |         | Yes      | One or more subreddits seperated by + signs                                                            |
| LIMIT         | 5       |          | How many posts to fetch on each refresh                                                                |
| INTERVAL      | 60      |          | Interval in seconds between each refresh                                                               |
| APPRISE_URLS  |         |          | [Apprise URLs](https://github.com/caronc/apprise#productivity-based-notifications) seperated by spaces |

# Config

The program looks for a `.env` file in the current directory.

# Docker

## Docker-compose

```yaml
version: "3"
services:
  subreddit-to-apprise:
    container_name: subreddit-to-apprise
    image: ghcr.io/itsnotgoodname/subreddit-to-apprise:latest
    environment:
      CLIENT_ID: XXXXXXXXXXXXXXXXXXXXXX
      CLIENT_SECRET: XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      SUBREDDITS: example1+example2
    restart: unless-stopped
```

## Docker CLI

```shell
docker run -d \
  --name=subreddit-to-apprise \
  -e CLIENT_ID=XXXXXXXXXXXXXXXXXXXXXX \
  -e CLIENT_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX \
  -e SUBREDDITS=example1+example2 \
  --restart unless-stopped \
  ghcr.io/itsnotgoodname/subreddit-to-apprise:latest
```

# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [0.1.1] - 2022-11-22

### Fix

- Repeated notifications when a post is deleted

## [0.1.0] - 2022-11-20

### Added

- First release
