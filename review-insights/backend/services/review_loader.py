import json
import os

BASE_PATH = os.path.dirname(os.path.dirname(__file__))

def get_reviews(product: str):
    file_path = os.path.join(
        BASE_PATH, "data", "products", f"{product}.json"
    )

    if not os.path.exists(file_path):
        return []

    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return data