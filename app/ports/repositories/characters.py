from abc import ABC, abstractmethod
from app.domain.entities.characters import Characters


class CharactersRepository(ABC):

    @abstractmethod
    def create(self, characters: Characters) -> bool:
        pass
