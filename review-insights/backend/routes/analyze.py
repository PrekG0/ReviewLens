from fastapi import APIRouter
from services.review_loader import get_reviews

router = APIRouter()

@router.get("/analyze")
def analyze(product: str):
    reviews = get_reviews(product)

    return {
        "product": product,
        "num_reviews": len(reviews),
        "sample": reviews[:3]
    }