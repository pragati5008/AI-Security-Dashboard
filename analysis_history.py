history = []

def add_record(url, risk):
    history.append({
        "URL": url,
        "Risk Score": risk
    })

def get_history():
    return history