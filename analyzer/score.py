def calculate_score(onpage, technical):
    score = 0

    if onpage["title"]:
        score += 20
    if onpage["meta_description"]:
        score += 20
    if onpage["h1_count"] == 1:
        score += 20
    if technical["https"]:
        score += 20
    if onpage["total_images"] > 0:
        alt_ratio = 1 - (onpage["images_without_alt"] / onpage["total_images"])
        if alt_ratio >= 0.8:
            score += 20

    return score
