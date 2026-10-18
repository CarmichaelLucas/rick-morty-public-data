import logging
from sqlalchemy.orm import Session

from app.ports.repositories.characters import CharactersRepository
from app.domain.entities.characters import Characters as Entity
from app.infrastructure.models import Characters


class InCharactersRepository(CharactersRepository):
    def __init__(self, session: Session) -> None:
        self.session = session

    def create(self, character: Entity) -> bool:
        try:
            model = Characters(
                name=character.name,
                status=character.status,
                species=character.species,
                gender=character.gender,
                external_id=character.external_id
            )
            self.session.add(model)
            self.session.commit()

            return True
        except Exception as e:
            logging.error(f'Error creating Character: {str(e)}')
            return False
