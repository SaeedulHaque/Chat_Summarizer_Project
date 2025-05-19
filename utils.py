import re
from collections import Counter, defaultdict
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
nltk.download('stopwords', quiet=True)
from nltk.corpus import stopwords

STOPWORDS = set(stopwords.words('english'))

def parse_chat_log(text):
    speaker_msgs = defaultdict(list)
    current_speaker = None
    for line in text.splitlines():
        match = re.match(r"^(\w+):\s*(.*)$", line)
        if match:
            current_speaker = match.group(1)
            message = match.group(2)
            speaker_msgs[current_speaker].append(message)
        else:
            if current_speaker and line.strip():
                speaker_msgs[current_speaker][-1] += " " + line.strip()
    return dict(speaker_msgs)

def get_message_stats(speaker_msgs):
def extract_keywords(messages, use_tfidf=True, top_n=5):
def generate_summary(stats, keywords, convo_summary):