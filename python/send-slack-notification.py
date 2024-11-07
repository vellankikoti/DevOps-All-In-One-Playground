import requests

def send_slack_notification(webhook_url, message):
    requests.post(webhook_url, json={"text": message})

send_slack_notification('your_webhook_url', 'Hello, DevOps team!')
