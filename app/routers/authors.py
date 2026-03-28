from typing import Annotated

from fastapi import APIRouter, Query

from app.dependencies import get_db
from app.crud.author import get_authors
from app.schemas.author import AuthorsResponse

router = APIRouter(tags=["authors"])


@router.get("/api/authors", response_model=AuthorsResponse, status_code=200)
async def get_authors_view(
    search: Annotated[str, Query()] = "",
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=0, le=100)] = 20,
):
    db = next(get_db())

    authors = get_authors(db, search, skip, limit)

    response = AuthorsResponse(
        limit=limit, skip=skip, search=search, count=len(authors), result=authors
    )

    return response
