from src.main import Entity


def test_entity_id_count():
    entity_one = Entity()
    entity_two = Entity()
    assert entity_one.id == 0 and entity_two.id == 1
