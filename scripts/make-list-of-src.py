#!/usr/bin/env python3

import csv
import sys

papers = dict()

with open(sys.argv[1]) as infile:
    reader = csv.reader(infile)
    next(reader, None)  # skip the headers
    for row in reader:
        author, title, _, _, affil = row
        papers[title] = (author, affil)

for paper in sorted(papers, key=lambda s: s.lower()):
    author, affil = papers[paper]
    print(f'<b>{paper}</b><br/>\n{author} ({affil})<br/><br/>\n')
