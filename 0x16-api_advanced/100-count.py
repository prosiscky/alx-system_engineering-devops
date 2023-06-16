#!/usr/bin/python3
"""
Write a recursive function that queries the Reddit API, parses the title
of all hot articles, and prints a sorted count of given keywords
(case-insensitive, delimited by spaces. Javascript should count as
javascript, but java should not).

Requirements:

Prototype: def count_words(subreddit, word_list)
Note: You may change the prototype, but it must be able to be called with
just a subreddit supplied and a list of keywords. AKA you can add a counter
or anything else, but the function must work without supplying a starting
value in the main.
If word_list contains the same word (case-insensitive), the final count should
be the sum of each duplicate (example below with java)
Results should be printed in descending order, by the count, and if the count
is the same for separate keywords, they should then be sorted alphabetically
(ascending, from A to Z). Words with no matches should be skipped and not
printed. Words must be printed in lowercase.
Results are based on the number of times a keyword appears, not titles it
appears in. java java java counts as 3 separate occurrences of java.
To make life easier, java. or java! or java_ should not count as java
If no posts match or the subreddit is invalid, print nothing.
NOTE: Invalid subreddits may return a redirect to search results. Ensure that
you are NOT following redirects.
Your code will NOT pass if you are using a loop and not recursively calling the
function! This /can/ be done with a loop but the point is to use a recursive
function. :)

Disclaimer: number presented in this example cannot be accurate now - Reddit
is hot articles are always changing
"""
import requests


def count_words(subreddit, word_list, hot_list=[], after=None):
    """
    Queries the Reddit API, parses the title of all hot articles,
    and prints a sorted count of given keywords.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Fake Agent"}
    params = {'after': after} if after else {}

    response = requests.get(url, headers=headers, params=params)
    data = response.json()

    if response.status_code == 200:
        for post in data['data']['children']:
            title = post['data']['title'].lower()
            words = title.split()

            for word in words:
                # Remove punctuation at the end of words
                word = word.rstrip('.!_')

                # Count the occurrences of matching keywords
                if word.lower() in word_list:
                    hot_list.append(word.lower())

        after = data['data']['after']

        if after:
            return count_words(subreddit, word_list, hot_list, after)
        else:
            word_count = {}

            for word in hot_list:
                if word not in word_count:
                    word_count[word] = 1
                else:
                    word_count[word] += 1

            sorted_words = sorted(
                    word_count.items(), key=lambda x: (-x[1], x[0]))

            for word, count in sorted_words:
                print("{}: {}".format(word, count))
    else:
        print("Invalid subreddit or no posts found.")
