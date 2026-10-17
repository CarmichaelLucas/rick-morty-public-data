from sqlalchemy import create_engine

from app.infrastructure.models import (
    Base, Characters, Episodes, Locations, EpisodesByCharacters, LocationsByCharacters
)


if __name__ == "__main__":
    engine = create_engine("sqlite:///etl.db", echo=True)
    Base.metadata.create_all(engine)
