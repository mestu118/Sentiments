import nltk

class Analyzer():
    """Implements sentiment analysis."""

    def __init__(self, positives, negatives):
        """Initialize Analyzer."""
        positiveFiles = open(positives, "r")
        negativeFiles = open(negatives,"r")
        self.positiveWords = set()
        self.negativeWords = set()
        for words in positiveFiles:
            if words.startswith(';'):
                continue
            self.positiveWords.add(words.strip())
        for words in negativeFiles:
            if words.startswith(';'):
                continue
            self.negativeWords.add(words.strip())


        # TODO

    def analyze(self, text):
        """Analyze text for sentiment, returning its score."""
        positive = 0
        negative = 0
        tokenizer = nltk.tokenize.TweetTokenizer()
        tokens = tokenizer.tokenize(text)
        for word in tokens:
            booty = str.lower(word)
            if booty in self.negativeWords:
                negative = negative + 1
            elif booty in self.positiveWords:
                positive = positive + 1
        if(positive > negative):
            return 1
        elif(negative > positive):
            return -1
        else:
            return 0