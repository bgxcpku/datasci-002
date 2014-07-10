import sys
import json

states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}

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


    state_scores = {}
    state_tweets = {}

    for line in tweet_file:
        tweet = json.loads(line)

        if not 'text' in tweet: continue
        if not 'place' in tweet: continue
        place = tweet['place']
        if place is None or (not 'full_name' in place): continue
        if place['country_code']<> 'US': continue

        state = place['full_name'].split(',')[1].strip()

        if not state in states: continue

        words = tweet['text'].split()

        tweet_score = 0

        for word in words:
            if word in scores: tweet_score += scores[word]

        if state in state_scores:
            state_scores[state] += tweet_score
            state_tweets[state] += 1
        else:
            state_scores[state] = tweet_score
            state_tweets[state] = 1

    happiest_state = ''
    highest_score = -999999

    for s in state_scores:
        ss = float(state_scores[s])/state_tweets[s]
        # print s, state_scores[s], state_tweets[s], ss
        if ss > highest_score:
            highest_score = ss
            happiest_state = s

    print happiest_state

if __name__ == '__main__':
    main()
