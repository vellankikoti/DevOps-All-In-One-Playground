import csv
import json

def csv_to_json(csv_file, json_file):
    with open(csv_file, mode='r') as file:
        csv_reader = csv.DictReader(file)
        data = [row for row in csv_reader]
    with open(json_file, mode='w') as file:
        json.dump(data, file)

csv_to_json('data.csv', 'data.json')
