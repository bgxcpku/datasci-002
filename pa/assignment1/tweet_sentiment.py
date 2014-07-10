import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = parse_sent_file(sent_file)
    for line in tweet_file:
        tweet = json.loads(line)
        words = tweet['text'].split()
        s = 0
        for word in words:
            if word in scores: s += scores[word]
        print s

def parse_sent_file(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

if __name__ == '__main__':
    main()
