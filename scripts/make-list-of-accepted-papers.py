#!/usr/bin/env python3

import csv


papers = dict()

with open("cgo18-authors.csv") as infile:
  reader = csv.reader(infile)
  next(reader, None)  # skip the headers
  for row in reader:
    _, title, firstname, surname, _, affil, _ = row
    author = ' '.join((firstname, surname))
    if title not in papers:
      papers[title] = [(author, affil)]
    else:
      papers[title].append((author, affil))

for paper in sorted(papers, key=lambda s: s.lower()):
  print(f'<b>{paper}</b><br/>')
  current_affil = None
  for i, (author, affil) in enumerate(papers[paper]):
    if current_affil and affil != current_affil:
      print(f' ({current_affil})', end="")
      current_affil = affil
    elif not current_affil:
      current_affil = affil
    if i:
      print(', ', end="")
    print(author, end="")
  print(f' ({current_affil})<br/><br/>\n')
