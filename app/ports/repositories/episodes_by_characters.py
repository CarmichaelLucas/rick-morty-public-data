from abc import ABC, abstractmethod


class EpisodesByCharactersRepository(ABC):

    @abstractmethod
    def create_all(self, character_id: int, episode_ids: list[int]) -> bool:
        pass
