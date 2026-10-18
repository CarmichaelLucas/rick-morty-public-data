import logging
from sqlalchemy.orm import Session

from app.ports.repositories.locations import LocationsRepository
from app.domain.entities.locations import Locations as Entity
from app.infrastructure.models import Locations


class InLocationsRepository(LocationsRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, location: Entity) -> bool:
        try:
            model = Locations(
                name=location.name,
                type=location.type,
                dimension=location.dimension,
                external_id=location.external_id
            )
            self.session.add(model)
            self.session.commit()

            return True
        except Exception as e:
            logging.error(f'Error creating Locations: {str(e)}')
            return False
