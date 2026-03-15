def generate_recommendations(onpage, technical):
    recs = []

    if not onpage["title"]:
        recs.append("Add a title tag (50–60 characters).")

    if not onpage["meta_description"]:
        recs.append("Add a meta description (150–160 characters).")

    if onpage["h1_count"] == 0:
        recs.append("Add an H1 tag to define page topic.")
    elif onpage["h1_count"] > 1:
        recs.append("Use only one H1 tag per page.")

    if onpage["images_without_alt"] > 0:
        recs.append("Add alt text to images for SEO and accessibility.")

    if not technical["https"]:
        recs.append("Enable HTTPS using SSL certificate.")

    if not technical["robots_txt"]:
        recs.append("Add robots.txt file.")

    if not technical["sitemap"]:
        recs.append("Add sitemap.xml and submit to Google Search Console.")

    return recs
