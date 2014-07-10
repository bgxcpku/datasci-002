import sys
import json

def hw():
    print 'Hello, world!'

def lines(fp):
    print str(len(fp.readlines()))

def parse_sent_file(sent_file):
    scores = {} # initialize an empty dictionary
    for line in sent_file:
        term, score  = line.split("\t")  # The file is tab-delimited. "\t" means "tab character"
        scores[term] = int(score)  # Convert the score to an integer.
    return scores

def main():
    sent_file = open(sys.argv[1])
    tweet_file = open(sys.argv[2])
    scores = parse_sent_file(sent_file)

    term_pos_scores = {};
    term_neg_scores = {};

    terms = {}

    for line in tweet_file:
        tweet = json.loads(line)

        if not 'text' in tweet: continue

        words = tweet['text'].split()


        for word in words:
            if not word in scores:
                terms[word] = 1
                term_pos_scores[word] = 0
                term_neg_scores[word] = 0

    # reset input
    tweet_file.seek(0)

    for line in tweet_file:
        tweet = json.loads(line)
        if not 'text' in tweet: continue
        words = tweet['text'].split()
        pos = False
        neg = False

        for word in words:
            if word in scores:
                if scores[word] > 0: pos = True
                if scores[word] < 0: neg = True

        for term in terms:
            if term in words:
                if pos : term_pos_scores[term]+=1
                if neg : term_neg_scores[term]+=1

    for term in terms:
        p = term_pos_scores[term]
        n = term_neg_scores[term]
        if n == 0 : print term, 0
        else : print term, float(p)/n


if __name__ == '__main__':
    main()
