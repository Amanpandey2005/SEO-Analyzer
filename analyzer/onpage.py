from bs4 import BeautifulSoup

def analyze_onpage(html):
    soup = BeautifulSoup(html, "lxml")

    title = soup.title.string.strip() if soup.title else None

    meta_desc = None
    tag = soup.find("meta", attrs={"name": "description"})
    if tag and tag.get("content"):
        meta_desc = tag["content"].strip()

    h1_tags = soup.find_all("h1")

    images = soup.find_all("img")
    images_without_alt = sum(1 for img in images if not img.get("alt"))

    return {
        "title": title,
        "title_length": len(title) if title else 0,
        "meta_description": meta_desc,
        "meta_length": len(meta_desc) if meta_desc else 0,
        "h1_count": len(h1_tags),
        "images_without_alt": images_without_alt,
        "total_images": len(images)
    }
