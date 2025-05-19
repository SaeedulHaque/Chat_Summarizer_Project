import os
import argparse
from transformers import pipeline
from utils import (
    parse_chat_log,
    get_message_stats,
    extract_keywords,
    generate_summary
)

def load_bart(model_id="lidiya/bart-large-xsum-samsum", device=-1):
    return pipeline("summarization", model=model_id, device=device)

def summarize_folder(input_dir, output_dir,
                     use_tfidf=True,
                     use_bart=False,
                     bart_model="lidiya/bart-large-xsum-samsum",
                     bart_device=-1):
    os.makedirs(output_dir, exist_ok=True)
    bart = load_bart(bart_model, bart_device) if use_bart and load_bart else None

    for fn in os.listdir(input_dir):
        if not fn.endswith(".txt"):
            continue
        path_in = os.path.join(input_dir, fn)
        text = open(path_in, 'r', encoding='utf-8').read()
        #stats
        speaker_msgs = parse_chat_log(text)
        stats = get_message_stats(speaker_msgs)
        all_msgs = [m for msgs in speaker_msgs.values() for m in msgs]
        keywords = extract_keywords(all_msgs, use_tfidf=use_tfidf)

if __name__ == "__main__":


    summarize_folder(
        args.input_dir,
        args.output_dir,
        use_tfidf=not args.no_tfidf,
        use_bart=args.use_bart,
        bart_model=args.bart_model,
        bart_device=args.bart_device
    )
