import os
import sys
import argparse
from utils import (
    parse_chat_log,
    get_message_stats,
    extract_keywords,
    generate_summary
)
def summarize_folder(input_dir, output_dir,
                     use_tfidf=True,
                     use_bart=False,
                     bart_model="lidiya/bart-large-xsum-samsum",
                     bart_device=-1):
    p.add_argument
if __name__ == "__main__":
     summarize_folder(
        args.input_dir,
        args.output_dir,
        use_tfidf=not args.no_tfidf,
        use_bart=args.use_bart,
        bart_model=args.bart_model,
        bart_device=args.bart_device
    )
