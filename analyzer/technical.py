import requests
from urllib.parse import urlparse

def analyze_technical(url):
    parsed = urlparse(url)

    https = parsed.scheme == "https"

    robots = False
    sitemap = False

    try:
        if requests.get(f"{parsed.scheme}://{parsed.netloc}/robots.txt").status_code == 200:
            robots = True
    except:
        pass

    try:
        if requests.get(f"{parsed.scheme}://{parsed.netloc}/sitemap.xml").status_code == 200:
            sitemap = True
    except:
        pass

    return {
        "https": https,
        "robots_txt": robots,
        "sitemap": sitemap
    }
