from abc import ABC, abstractmethod
from app.domain.entities.locations import Locations


class LocationsRepository(ABC):

    @abstractmethod
    def create(self, locations: Locations) -> bool:
        pass
