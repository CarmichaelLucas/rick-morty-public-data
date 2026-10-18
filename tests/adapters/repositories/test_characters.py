from app.adapters.repositories.characters import InCharactersRepository
from app.domain.entities.characters import Characters as Entity


def test_create_character_in_db(session):
    repo = InCharactersRepository(session=session)
    entity = Entity(
        name='Rick Sanchez',
        status='Alive',
        species='Human',
        gender='Male',
        external_id=1
    )

    result = repo.create(character=entity)
    assert result == True


def test_not_create_character_in_db(session):
    repo = InCharactersRepository(session=session)
    entity = Entity()

    result = repo.create(character=entity)
    assert result is False
