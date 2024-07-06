"""Schema for AI Resume API"""
from pydantic import BaseModel
from typing import List


class User(BaseModel):
    id: int
    skills: List[str]
    location: str
    experience: int
    match_score: int = None


class MatchRequest(BaseModel):
    buyer: User
    freelancers: List[User]


class APIInput(BaseModel):
    """Input schema for AI Resume API"""
    user_id: str
    context: str


class Output(BaseModel):
    """Output schema for AI Resume API"""
    generated_content: str


class APIOutput(BaseModel):
    """API Output schema for AI Resume API"""
    user_id: str
    output: Output
