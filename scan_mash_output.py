#!/usr/bin/env python3

import argparse
import re

MASH_SKETCH_MSG_PATTERN = r'^Sketching .+ \(provide sketch file made with "mash sketch" to skip\).+$'
MASH_OUTPUT_PATTERN = r'^(.+)\s+(.+)\s+(\d+(\.\d+)?(e\-\d+)?)\s+(\d+(\.\d+)?(e\-\d+)?)\s+(\d+)\/(\d+)$'

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(dest='mash_file_path', help='Mash output file path')
    args = parser.parse_args()
    
    mash_output_count = 0
    mash_error_count = 0
    
    with open(args.mash_file_path) as f:
        for line in f.readlines():
            line_msg = line.rstrip()
            if re.match(MASH_SKETCH_MSG_PATTERN, line_msg):
                continue
            
            if re.match(MASH_OUTPUT_PATTERN, line_msg):
                mash_output_count += 1
                continue
            
            print(line_msg)
            mash_error_count += 1
            
    print(f'Number of mash output lines processed = {mash_output_count}')
    print(f'Number of mash errors found = {mash_error_count}')
