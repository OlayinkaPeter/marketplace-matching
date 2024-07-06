# Define the weights for each criterion
weights = {
    "skills": 0.5,
    "location": 0.3,
    "experience": 0.2
}

# Example data
freelancers_ = [
    {"id": 1, "skills": ["python", "fastapi"], "location": "NY", "experience": 5},
    {"id": 2, "skills": ["java", "spring"], "location": "SF", "experience": 3},
    {"id": 3, "skills": ["python", "flask"], "location": "NY", "experience": 2}
]

buyer_ = {"id": 4, "skills": ["python"], "location": "NY", "experience": 4}


# Define scoring functions
def score_skills(buyer_skills, freelancer_skills):
    return len(set(buyer_skills) & set(freelancer_skills)) / len(set(buyer_skills) | set(freelancer_skills))


def score_location(buyer_location, freelancer_location):
    return 1 if buyer_location == freelancer_location else 0


def score_experience(buyer_experience, freelancer_experience):
    return min(buyer_experience / freelancer_experience, 1) if freelancer_experience != 0 else 0


# Calculate match score
def calculate_match_score(buyer, freelancer):
    skills_score = score_skills(buyer.skills, freelancer.skills) * weights["skills"]
    location_score = score_location(buyer.location, freelancer.location) * weights["location"]
    experience_score = score_experience(buyer.experience, freelancer.experience) * weights["experience"]

    total_score = skills_score + location_score + experience_score
    return total_score
