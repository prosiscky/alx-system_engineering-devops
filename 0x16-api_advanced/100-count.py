#!/usr/bin/python3
"""a recursive function that queries the Reddit API, parses
    the title of all hot articles, and prints a sorted count
    of given keywords
"""
import requests


def count_words(subreddit, word_list, kwargs={}, after=None):
    """Recursively query the Reddit API, parse the titles of all hot articles,
    and count the occurrence of given keywords. Print the count in descending
    order of occurrence, then alphabetically if the count is the same.

    Args:
        subreddit (str): The name of the subreddit to query.
        word_list (List[str]): The list of keywords to count.
        count_dict (Dict[str, int], optional): The dictionary
        of keyword counts.

            Defaults to None, which creates an empty dictionary.
        after (str, optional): The Reddit API parameter to get the
        next page of results.

            Defaults to None, which gets the first page of results.

    Returns:
        None
    """
    url = "https://www.reddit.com/r/{}/hot/.json?after={}".format(
                        subreddit, after)
    headers = {"User-Agent": "custom"}

    data = requests.get(url, headers=headers, allow_redirects=False)
    if data.status_code == 200:
        after = data.json().get("data").get("after")
        data = data.json().get("data").get("children")
        for entry in data:
            parse_list = entry.get("data").get("title").lower().split()
            for word in parse_list:
                for element in word_list:
                    if word == element:
                        if element in kwargs:
                            kwargs[element] += 1
                        else:
                            kwargs[element] = 1
        if after:
            count_words(subreddit, word_list, kwargs, after)
        else:
            sorted_dict = {k: v for k, v in sorted(kwargs.items(),
                           key=lambda item: item[1])}
            [print("{}: {}".format(k, v)) for k, v in sorted_dict.items()]
    else:
        return (None)
