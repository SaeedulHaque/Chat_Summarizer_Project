# Chat Log Summarizer

A Python project to analyze and summarize multi-speaker chat logs. It produces a concise text summary including total message stats and topic keywords (via TF-IDF or frequency)
---

## Contents

- [Overview](#overview)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [File Structure](#file-structure)
- [Usage](#usage)
- [Functions Explained](#functions-explained)
- [Example](#example)
- [Improvement option - BART Summarization](#bart-summarization)

---

## Overview

This script helps in understanding large `.txt` chat logs by breaking them down into:
- Message counts
- Frequent or relevant keywords
- Topic summaries (keyword-based or abstractive)

It’s useful for:
- Analyzing chatbot conversations
- Summarizing customer service chats
- Condensing lengthy discussions into bullet points

---

## How It Works

1. Reads `.txt` chat logs from a specified folder.
2. Parses speakers and messages line-by-line.
3. Computes:
   - Total messages
   - Messages per speaker
4. Extracts keywords using:
   - **TF-IDF** (by default), or
   - Word frequency (`--no-tfidf`)
5. Generates a text-based topic summary:
   - Using top keywords (`default`)
   - Or using BART summarization (`optional`)
6. Writes everything into a new file.

---

## File Structure
```
chat-log-summarizer/
|
|- summarize.py - Main script
|- utils.py - Helper functions
|- logs/ - Folder for input .txt chat logs
|- summaries/ - Folder for output summary files
```
---

## Installation

```bash
git clone https://github.com/yourusername/chat-log-summarizer.git
cd chat-log-summarizer
pip install -r requirements.txt
```
## Usage
Using TF-IDF
```bash
python summarize.py logs summaries
```
---
## Functions Explained
### From utils.py:

**parse_chat_log(text: str) -> dict**

-Parses each line as Speaker: Message

-Returns a dictionary: {speaker_name: [msg1, msg2, ...]}

**get_message_stats(speaker_msgs: dict) -> dict**

-Counts total and per-speaker messages

-Example: { 'total_messages': 10, 'User_messages': 6, 'AI_messages': 4 }

**extract_keywords(messages: list, use_tfidf=True, top_n=5) -> list**

-Tokenizes all messages

-Removes stopwords

-Extracts top N keywords using:

1. TfidfVectorizer (if use_tfidf=True)

**joined = " ".join(messages)**

-Combines all chat messages into one string.

**vec = TfidfVectorizer(stop_words='english', max_features=top_n)**

-Initializes the TF-IDF vectorizer.

-Removes common English stopwords (like the, is, and).

-Keeps only the top top_n highest-scoring keywords.

**vec.fit([joined])**

-Learns the vocabulary from this single document (the chat log).

-Calculates the TF-IDF score for each word.

**vec.get_feature_names_out()**

-Retrieves the top keywords by TF-IDF score

2. Counter frequency (if False)

**generate_summary(stats: dict, keywords: list, convo_summary: str) -> str**

-Formats the full summary as a printable string

### From summarize.py:

**summarize_folder(...)**

-Core runner

-Iterates over input files

-Runs parse_chat_log, get_message_stats, extract_keywords

-Generates keyword or BART-based summary

-Writes final summary to file

## Example
### Input Image
![Image](https://github.com/user-attachments/assets/06c50d0c-3e94-41b1-8d0c-26ee7e31146c)
### Output Image
![Image](https://github.com/user-attachments/assets/29e4ab27-8362-4f5e-a280-2d2663d6dd36)
