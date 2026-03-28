from typing import List

from sqlalchemy import or_
from sqlalchemy.orm import Session

from app.models.author import Author


def get_authors(
    db: Session, search: str = "", offset: int = 0, limit: int = 20
) -> List[Author]:
    q = db.query(Author)

    if search != "":
        pattern = f"%{search}%"

        q = q.filter(
            or_(
                Author.first_name.ilike(pattern),
                Author.last_name.ilike(pattern),
            )
        )

    authors = q.offset(offset).limit(limit).all()

    return authors
