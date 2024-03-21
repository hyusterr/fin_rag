import argparse
from retriever.cnc_alignment import CncAlignment
from utils.utils import read_jsonl

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Retrieval of CnC alignment')
    parser.add_argument('--target_jsonl', '-t', type=str, help='Input file')
    parser.add_argument('--output_trec', '-o', type=str, help='Output file')
    
    args = parser.parse_args()
    cnc_alignment = CncAlignment()
    data = read_jsonl(args.target_jsonl)
    cnc_alignment.run(args.target_jsonl, args.output_trec)
