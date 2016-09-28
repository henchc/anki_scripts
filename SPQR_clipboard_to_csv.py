import csv
import tkinter as tk

root = tk.Tk()

# keep the window from showing
root.withdraw()

# read the clipboard
words = root.clipboard_get().split("\n\n")

words_filtered = [tuple(l.split("\n"))
                  for l in words if "unknown" not in l.lower() and len(l) > 1]

with open("to_anki.csv", "w") as f:
    csv_writer = csv.writer(f)
    for w in words_filtered:
        csv_writer.writerow(w)
