#!/usr/bin/env python

import praw
r = praw.Reddit(user_agent='this_is_a_test_script')
f = open('list_of_links.txt', 'a')

# Change subreddit:
SUBREDDIT = 'lotr'

# Change keyword:
KEYWORD = 'wiki'

KEYWORD = KEYWORD.lower()
print 'Now searching! This may take a moment.'
subreddit = r.get_subreddit(SUBREDDIT)
comments = subreddit.get_comments(limit = 1000) # Cap

i = 0

for comment in comments:
    i += 1
    if 'wiki' in comment.body.lower():
        try:
            f.write(comment.permalink + '?context=3\n')
        except:
            print "There was an error!"

print 'Done with %d hits!' % i
