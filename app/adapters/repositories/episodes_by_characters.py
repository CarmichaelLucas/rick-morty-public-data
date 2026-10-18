import logging
from sqlalchemy.orm import Session

from app.ports.repositories.episodes_by_characters import EpisodesByCharactersRepository
from app.infrastructure.models import EpisodesByCharacters


class InEpisodesByCharacters(EpisodesByCharactersRepository):
    def __init__(self, session: Session):
        self.session = session

    def create_all(self, character_id: int, episode_ids: list[int]) -> bool:
        try:
            models = [
                EpisodesByCharacters(
                    character_id=character_id,
                    episode_id=episode_id
                ) for episode_id in episode_ids
            ]

            self.session.add_all(models)
            self.session.commit()

            return True
        except Exception as e:
            logging.error(f'Error creating list for EpisodesByCharacters: {str(e)}')
            return False
