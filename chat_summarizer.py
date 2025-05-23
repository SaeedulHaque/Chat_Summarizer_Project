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
        #convo_summary
        if use_bart and bart:
            convo_summary = bart(
                "\n".join(all_msgs),
                max_length=150, min_length=40, do_sample=False
            )[0]["summary_text"]
        else:
            top2 = keywords[:2]
            if not top2:
                convo_summary = "No clear topic."
            elif len(top2) == 1:
                convo_summary = f"It focused mainly on {top2[0]}."
            else:
                convo_summary = f"It focused mainly on {top2[0]} and {top2[1]}."

        summary_text = generate_summary(stats, keywords, convo_summary)
        out_fn = fn.replace(".txt", "_summary.txt")
        with open(os.path.join(output_dir, out_fn), 'w', encoding='utf-8') as f:
            f.write(summary_text)
        
if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Chat Log Summarizer")
    p.add_argument("input_dir", help="Folder with .txt logs")
    p.add_argument("output_dir", help="Folder to write summaries")
    p.add_argument("--no-tfidf", action="store_true", help="Disable TF-IDF")
#    p.add_argument("--use-bart", action="store_true", help="Enable BART abstractive summary")
#    p.add_argument("--bart-model", default="lidiya/bart-large-xsum-samsum",help="Hugging Face model ID for BART")
#    p.add_argument("--bart-device", type=int, default=-1, help="-1 for CPU or GPU index")
    args = p.parse_args()
    summarize_folder(
        args.input_dir,
        args.output_dir,
        use_tfidf=not args.no_tfidf,
        use_bart=False
    )
