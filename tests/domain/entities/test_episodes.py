from app.domain.entities.episodes import Episodes


def test_entity_episodes_none():
    episode = Episodes()

    assert episode.id == None
    assert episode.name == ''
    assert episode.air_date == ''
    assert episode.code == ''
    assert episode.external_id == None


def test_entity_episodes_with_data():
    episode = Episodes(
        id=1,
        name='Pilot',
        air_date='December 2, 2013',
        code='S01E01',
        external_id=1
    )

    assert episode.id == 1
    assert episode.name == 'Pilot'
    assert episode.air_date == 'December 2, 2013'
    assert episode.code == 'S01E01'
    assert episode.external_id == 1
