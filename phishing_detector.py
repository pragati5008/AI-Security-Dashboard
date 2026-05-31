import re

def analyze_url(url):

    messages = []

    if "@" in url:
        messages.append("🚨 Contains @ symbol")

    if len(url) > 50:
        messages.append("⚠️ Very Long URL")

    if url.count(".") > 3:
        messages.append("⚠️ Too Many Dots")

    if re.search(r"\d+\.\d+\.\d+\.\d+", url):
        messages.append("🚨 IP Address Found")

    return messages