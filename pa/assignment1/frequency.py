import sys
import json


def main():
    tweet_file = open(sys.argv[1])

    terms = {}
    total = 0

    for line in tweet_file:
        tweet = json.loads(line)

        if not 'text' in tweet: continue

        words = tweet['text'].split()

        for word in words:

            total += 1

            if not word in terms:
                terms[word] = 1
            else:
                terms[word] += 1


    for term in terms:
        print term, float(terms[term]) / total

if __name__ == '__main__':
    main()
