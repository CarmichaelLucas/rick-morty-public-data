from dataclasses import dataclass


@dataclass
class Locations:
    id: int = None
    name: str = ''
    type: str = ''
    dimension: str = ''
    external_id: int = None
