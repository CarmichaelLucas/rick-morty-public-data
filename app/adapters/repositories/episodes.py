import logging
from sqlalchemy.orm import Session

from app.ports.repositories.episodes import EpisodesRepository
from app.domain.entities.episodes import Episodes as Entity
from app.infrastructure.models import Episodes


class InEpisodesReposotory(EpisodesRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, episode: Entity) -> bool:
        try:
            model = Episodes(
                name=episode.name,
                air_date=episode.air_date,
                code=episode.code,
                external_id=episode.external_id
            )
            self.session.add(model)
            self.session.commit()

            return True
        except Exception as e:
            logging.error(f'Error creating Episodes: {str(e)}')
            return False
