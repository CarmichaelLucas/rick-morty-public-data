from app.domain.entities.characters import Characters


def test_entity_character_none():
    character = Characters()

    assert character.id == None
    assert character.name == ''
    assert character.status == ''
    assert character.species == ''
    assert character.gender == ''
    assert character.external_id == None


def test_entity_character_with_data():
    character = Characters(
        id=1,
        name='Rick Sanchez',
        status='Alive',
        species='Human',
        gender='Male',
        external_id=1
    )

    assert character.id == 1
    assert character.name == 'Rick Sanchez'
    assert character.status == 'Alive'
    assert character.species == 'Human'
    assert character.gender == 'Male'
    assert character.external_id == 1
