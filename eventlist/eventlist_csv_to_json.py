import csv
import json
 
keys = ['name', 'tagged', 'begin', 'end', 'status', 'source']
rows = []

with open('eventlist.csv', 'r', encoding='utf-8') as f:
  f.readline() # skip header

  reader = csv.DictReader(f, keys)

  for row in reader:
    del row['status']
    del row['source']
    rows.append(row)


with open('eventlist.json', 'w', encoding='utf-8') as f:
  json.dump(rows, f, indent=2, ensure_ascii=False)
