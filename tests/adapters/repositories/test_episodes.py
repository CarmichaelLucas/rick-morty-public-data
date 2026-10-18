from app.adapters.repositories.episodes import InEpisodesReposotory
from app.domain.entities.episodes import Episodes as Entity


def test_create_episode_in_db(session):
    repo = InEpisodesReposotory(session=session)
    entity = Entity(
        name='Pilot',
        air_date='December 2, 2013',
        code='S01E01',
        external_id=1
    )

    result = repo.create(episode=entity)
    assert result == True


def test_not_create_episode_in_db(session):
    repo = InEpisodesReposotory(session=session)
    entity = Entity()

    result = repo.create(episode=entity)
    assert result is False
