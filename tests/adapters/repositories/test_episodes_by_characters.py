from app.adapters.repositories.episodes_by_characters import InEpisodesByCharacters


def test_create_episodes_by_characters_in_db(session):
    repo = InEpisodesByCharacters(session=session)
    episode_ids = [1, 2, 3, 4]
    character_id = 1

    result = repo.create_all(character_id=character_id, episode_ids=episode_ids)
    assert result == True


def test_not_create_episodes_by_characters_in_db(session, mocker):
    repo = InEpisodesByCharacters(session=session)
    episode_ids = [1]
    character_id = 1

    mocker.patch.object(session, 'add_all', side_effect=Exception('Error'))

    result = repo.create_all(character_id=character_id, episode_ids=episode_ids)
    assert result is False
