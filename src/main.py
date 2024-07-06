"""Main module for the API Resume."""
from fastapi import FastAPI, status, HTTPException
from src.utils import calculate_match_score, buyer_, freelancers_
from src.schema import User, MatchRequest

TITLE = "Freelance Marketplace Matching"
DESCRIPTION = """
Olayinka Peter O. 🚀 
"""

app = FastAPI(
    title=TITLE,
    description=DESCRIPTION,
    version="0.1",
    redoc_url=None,
)


@app.post("/match")
def match_freelancers(request: MatchRequest):
    buyer = request.buyer
    freelancers = request.freelancers

    if not freelancers:
        raise HTTPException(status_code=400, detail="No freelancers provided")

    # Calculate scores for each freelancer
    for freelancer in freelancers:
        freelancer.match_score = calculate_match_score(buyer, freelancer)

    # Sort freelancers by match score in descending order
    sorted_freelancers = sorted(freelancers, key=lambda x: x.match_score, reverse=True)
    return {"matches": sorted_freelancers}


# Test endpoint
@app.get("/test_match")
def test_match():
    request = MatchRequest(buyer=buyer_, freelancers=freelancers_)
    return match_freelancers(request)
