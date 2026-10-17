from app.domain.entities.locations import Locations


def test_entity_locations_none():
    location = Locations()

    assert location.id == None
    assert location.name == ''
    assert location.type == ''
    assert location.dimension == ''
    assert location.external_id == None


def test_entity_locations_with_data():
    location = Locations(
        id=1,
        name='Earth',
        type='Planet',
        dimension='Dimension C-137',
        external_id=1
    )

    assert location.id == 1
    assert location.name == 'Earth'
    assert location.type == 'Planet'
    assert location.dimension == 'Dimension C-137'
    assert location.external_id == 1
