from abc import ABC, abstractmethod


class LocationsByCharactersRepository(ABC):

    @abstractmethod
    def create(
        self,
        character_id: int,
        original_location_id: int,
        actual_location_id: int
    ) -> bool:
        pass
