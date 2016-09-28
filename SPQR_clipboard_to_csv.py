import sys
import csv

fpath = sys.argv[1]

with open(fpath, "r") as f:
    raw = f.read()

words = raw.split("\n\n")

words_filtered = [tuple(l.split("\n"))
                  for l in words if "unknown" not in l.lower() and len(l) > 0]

with open("to_anki.csv", "w") as f:
    csv_writer = csv.writer(f)
    for w in words_filtered:
        csv_writer.writerow(w)
