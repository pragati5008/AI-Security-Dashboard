import re

def extract_features(url):

    features = {}

    # URL Length
    features["url_length"] = len(url)

    # Contains @
    features["has_at"] = 1 if "@" in url else 0

    # Contains IP
    features["has_ip"] = 1 if re.search(r"\d+\.\d+\.\d+\.\d+", url) else 0

    # HTTPS
    features["https"] = 1 if url.lower().startswith("https://") else 0

    # Number of dots
    features["dot_count"] = url.count(".")

    # Number of hyphens
    features["hyphen_count"] = url.count("-")

    # Number of digits
    features["digit_count"] = sum(c.isdigit() for c in url)

    return features