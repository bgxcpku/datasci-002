import sys
import json
import collections
import operator


def main():
    tweet_file = open(sys.argv[1])

    total = 0

    tags = {}

    for line in tweet_file:
        tweet = json.loads(line)

        if not 'entities' in tweet or tweet['entities'] is None: continue

        if not 'hashtags' in tweet['entities'] or tweet['entities']['hashtags'] is None: continue

        hashtags = tweet['entities']['hashtags']

        if len(hashtags) == 0 : continue

        for hashtag in hashtags:
            tag = hashtag['text']
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1

    sorted_x = sorted(tags.iteritems(), key=operator.itemgetter(1), reverse=True)

    n = 0
    for tag, c in sorted_x:
        print tag, c
        n+=1
        if n>=10: break
#

if __name__ == '__main__':
    main()
