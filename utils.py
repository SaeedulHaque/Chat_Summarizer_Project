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
#    stats = {}
#    for speaker, messages in speaker_msgs.items():
#        stats[speaker] = {
#            'message_count': len(messages),
#            'word_count': sum(len(msg.split()) for msg in messages),
#            'avg_word_count': sum(len(msg.split()) for msg in messages) / len(messages) if messages else 0,
#            'longest_message': max(messages, key=len) if messages else "",
#            'longest_message_length': len(max(messages, key=len)) if messages else 0
#        }
#    return stats
#print("Message stats:", get_message_stats(speaker_msgs))
    stats = {'total_messages': sum(len(msgs) for msgs in speaker_msgs.values())}
    for speaker, msgs in speaker_msgs.items():
        stats[f'{speaker}_messages'] = len(msgs)
    return stats

def extract_keywords(messages, use_tfidf=True, top_n=5):
    joined = " ".join(messages)
    tokens = re.findall(r"\b\w+\b", joined.lower())
    filtered = [w for w in tokens if w not in STOPWORDS]

    if use_tfidf:
        vec = TfidfVectorizer(stop_words='english', max_features=top_n)
        vec.fit([joined])
        return list(vec.get_feature_names_out())
    else:
        freq = Counter(filtered)
        return [word for word, _ in freq.most_common(top_n)]
    
def generate_summary(stats, keywords, convo_summary):
    total = stats['total_messages']
    kwords_line = ', '.join(keywords) if keywords else 'None'
    lines = [
        "Summary:",
        f"- The number of exchanges in the conversation: {total}",
        f"- Summary of the conversation: {convo_summary}",
        f"- Most common keywords: {kwords_line}"
    ]
    return "\n".join(lines) + "\n"