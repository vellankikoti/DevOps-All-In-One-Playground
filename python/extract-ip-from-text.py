import re

def extract_ips(text):
    return re.findall(r'\b(?:[0-9]{1,3}\.){3}[0-9]{1,3}\b', text)

sample_text = "Here are some IPs: 192.168.1.1, 10.0.0.5, and an invalid IP 999.999.999.999"
print(extract_ips(sample_text))
