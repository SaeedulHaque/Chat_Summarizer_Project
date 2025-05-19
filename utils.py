from collections import Counter, defaultdict
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def parse_chat_log(text):
def get_message_stats(speaker_msgs):
def extract_keywords(messages, use_tfidf=True, top_n=5):
def generate_summary(stats, keywords, convo_summary):