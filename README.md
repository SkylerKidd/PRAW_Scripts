# PRAW_Scripts
A collection of test scripts using PRAW, a Python wrapper for the Reddit API.

## Setup
1. Install [Python 2.7](https://www.python.org/downloads/)
2. Run `pip install praw` in terminal/command line

## Usage

### Keyword Search
This script goes through the 1000 most recent comments for a given subreddit and prints a list of permalinks to comments than contain a given keyword.
1. Set the values for `SUBREDDIT` and `KEYWORD` as desired in keyword_search.py
2. Run `python keyword_search.py` in terminal/command line
3. Open list_of_links.txt, which will have been created in the current directory
