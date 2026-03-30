def process_reviews(reviews):
    cleaned_reviews = []

    for review in reviews:
        text = review.get("text", "").strip()

        if text:
            cleaned_reviews.append(text)

    return cleaned_reviews
