from textblob import TextBlob
def download_corpora():
    try:
        # Check if corpora are already downloaded
        nltk.data.find('corpora/brown.zip')
        nltk.data.find('tokenizers/punkt')
        nltk.data.find('corpora/wordnet.zip')
        nltk.data.find('taggers/averaged_perceptron_tagger.zip')
    except LookupError:
        # If not found, download the required corpora
        nltk.download('brown', quiet=True)
        nltk.download('punkt', quiet=True)
        nltk.download('wordnet', quiet=True)
        nltk.download('averaged_perceptron_tagger', quiet=True)
