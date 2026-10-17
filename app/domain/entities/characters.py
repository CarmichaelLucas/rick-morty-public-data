from dataclasses import dataclass


@dataclass
class Characters:
    id: int = None
    name: str = ''
    status: str = ''
    species: str = ''
    gender: str = ''
    external_id: int = None
