from app.adapters.repositories.locations_by_characters import InLocationsByCharacters


def test_create_locations_by_characters_in_db(session):
    repo = InLocationsByCharacters(session=session)
    origin_location_id = 1
    actual_location_id = 1
    character_id = 1

    result = repo.create(
        character_id=character_id,
        origin_location_id=origin_location_id,
        actual_location_id=actual_location_id
    )
    assert result == True


def test_not_create_locations_by_characters_in_db(session, mocker):
    repo = InLocationsByCharacters(session=session)
    origin_location_id = 1
    actual_location_id = 1
    character_id = 1

    mocker.patch.object(session, 'add', side_effect=Exception('Error'))

    result = repo.create(
        character_id=character_id,
        origin_location_id=origin_location_id,
        actual_location_id=actual_location_id
    )
    assert result is False
