from dataclasses import dataclass


@dataclass
class Episodes:
    id: int = None
    name: str = ''
    air_date: str = ''
    code: str = ''
    external_id: int = None
