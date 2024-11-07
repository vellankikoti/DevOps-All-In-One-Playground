import json

def urls_to_json(file_path):
    with open(file_path, 'r') as file:
        urls = [line.strip() for line in file if line.startswith('http')]
    with open('urls.json', 'w') as json_file:
        json.dump(urls, json_file)

urls_to_json('urls.txt')
