from abc import ABC, abstractmethod
from app.domain.entities.episodes import Episodes


class EpisodesRepository(ABC):

    @abstractmethod
    def create(self, episodes: Episodes) -> bool:
        pass
