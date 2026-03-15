import requests

def fetch_html(url, timeout=10):
    try:
        headers = {
            "User-Agent": "Mozilla/5.0 SEO-Analyzer"
        }
        response = requests.get(url, headers=headers, timeout=timeout)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        return None
