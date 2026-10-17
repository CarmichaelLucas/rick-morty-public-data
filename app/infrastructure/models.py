from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase


class Base(DeclarativeBase):
    pass


class Characters(Base):
    __tablename__ = "characters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    status: Mapped[str] = mapped_column(String, nullable=False)
    species: Mapped[str] = mapped_column(String, nullable=False)
    gender: Mapped[str] = mapped_column(String, nullable=False)
    external_id: Mapped[int] = mapped_column(Integer, nullable=False)


class Episodes(Base):
    __tablename__ = "episodes"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    air_date: Mapped[str] = mapped_column(String, nullable=False)
    code: Mapped[str] = mapped_column(String, nullable=False)
    external_id: Mapped[int] = mapped_column(Integer, nullable=False)


class Locations(Base):
    __tablename__ = "locations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    type: Mapped[str] = mapped_column(String, nullable=False)
    dimension: Mapped[str] = mapped_column(String, nullable=False)
    external_id: Mapped[int] = mapped_column(Integer, nullable=False)


class EpisodesByCharacters(Base):
    __tablename__ = "episodes_by_characters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    character_id: Mapped[int] = mapped_column(
        ForeignKey("characters.id"),
        nullable=False,
    )
    episode_id: Mapped[int] = mapped_column(
        ForeignKey("episodes.id"),
        nullable=False,
    )


class LocationsByCharacters(Base):
    __tablename__ = "locations_by_characters"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    character_id: Mapped[int] = mapped_column(
        ForeignKey("characters.id"),
        nullable=False,
    )
    origin_location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id"),
        nullable=False,
    )
    actual_location_id: Mapped[int] = mapped_column(
        ForeignKey("locations.id"),
        nullable=False,
    )
