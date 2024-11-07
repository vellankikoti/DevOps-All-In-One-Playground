import requests

def parse_json_from_url(url):
    response = requests.get(url)
    data = response.json()
    print(json.dumps(data, indent=4))

parse_json_from_url('https://jsonplaceholder.typicode.com/posts/1')
