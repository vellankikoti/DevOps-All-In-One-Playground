import requests

def download_file(url, file_path):
    response = requests.get(url)
    with open(file_path, 'wb') as file:
        file.write(response.content)
    print(f"Downloaded {url} to {file_path}")

download_file('https://example.com/file.txt', 'file.txt')
