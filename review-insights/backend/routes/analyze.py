from fastapi import APIRouter
from services.review_loader import get_reviews
from services.processor import process_reviews
from services.llm_service import analyze_reviews_with_llm

router = APIRouter()

@router.get("/analyze")
def analyze(product: str):
    reviews = get_reviews(product)
    processed = process_reviews(reviews)

    insights = analyze_reviews_with_llm(processed)

    return {
        "product": product,
        "num_reviews": len(reviews),
        **insights
    }