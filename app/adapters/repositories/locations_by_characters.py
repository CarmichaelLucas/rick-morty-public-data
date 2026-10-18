import logging
from sqlalchemy.orm import Session

from app.ports.repositories.locations_by_characters import LocationsByCharactersRepository
from app.infrastructure.models import LocationsByCharacters


class InLocationsByCharacters(LocationsByCharactersRepository):
    def __init__(self, session: Session):
        self.session = session

    def create(
        self,
        character_id: int,
        origin_location_id: int,
        actual_location_id: int
    ) -> bool:
        try:
            model = LocationsByCharacters(
                character_id=character_id,
                origin_location_id=origin_location_id,
                actual_location_id=actual_location_id
            )

            self.session.add(model)
            self.session.commit()

            return True
        except Exception as e:
            logging.error(f'Error creating for LocationsByCharacters: {str(e)}')
            return False
