from app.adapters.repositories.locations import InLocationsRepository
from app.domain.entities.locations import Locations as Entity


def test_create_location_in_db(session):
    repo = InLocationsRepository(session=session)
    entity = Entity(
        name='Earth',
        type='Planet',
        dimension='Dimension C-137',
        external_id=1
    )

    result = repo.create(location=entity)
    assert result == True


def test_not_create_location_in_db(session):
    repo = InLocationsRepository(session=session)
    entity = Entity()

    result = repo.create(location=entity)
    assert result is False
